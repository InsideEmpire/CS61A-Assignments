import argparse
import json
import socketserver
import ssl
import time
import traceback
import webbrowser
import os
from functools import wraps
from http import HTTPStatus, server
from http.server import HTTPServer
from urllib.error import URLError
from urllib.parse import unquote, urlparse, parse_qs
from urllib.request import Request, urlopen

STATIC_PATHS = {}
PATHS = {}
# 
CONTENT_TYPE_LOOKUP = dict(
    html="text/html",
    css="text/css",
    js="application/javascript",
    svg="image/svg+xml",
    gif="image/gif",
    ico="image/x-icon",
)


def path_optional(decorator):
    def wrapped(func_or_path):
        if callable(func_or_path):
            return decorator("/" + func_or_path.__name__)(func_or_path)
        else:

            def actual_decorator(f):
                return decorator(func_or_path)(f)

            return actual_decorator

    return wrapped


def route(path):
    """Register a route handler."""

    if callable(path):
        return route("/" + path.__name__)(path)

    if not path.startswith("/"):
        path = "/" + path

    def wrap(f):
        if "." in path:
            STATIC_PATHS[path] = f
        else:
            PATHS[path] = f
        return f

    return wrap


class Handler(server.BaseHTTPRequestHandler):
    """HTTP handler."""

    def do_GET(self):
        try:
            parsed_url = urlparse(unquote(self.path))
            path = parsed_url.path
            query_params = parse_qs(parsed_url.query)

            if path in STATIC_PATHS:
                out = bytes(STATIC_PATHS[path](**snakify(query_params)), "utf-8")
            else:
                path = GUI_FOLDER + path[1:]
                if "scripts" in path and not path.endswith(".js"):
                    path += ".js"
                if path == GUI_FOLDER:
                    path = GUI_FOLDER + "index.html"
                with open(path, "rb") as f:
                    out = f.read()
        except FileNotFoundError:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.end_headers()
        except Exception as e:
            print(e)
            self.send_response(HTTPStatus.INTERNAL_SERVER_ERROR)
            self.end_headers()
        else:
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", CONTENT_TYPE_LOOKUP[path.split(".")[-1]])
            self.end_headers()
            self.wfile.write(out)

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        raw_data = self.rfile.read(content_length).decode("utf-8")
        data = json.loads(raw_data)
        path = unquote(self.path)

        try:
            result = PATHS[path](**snakify(data))
        except Exception as e:
            print(e)
            self.send_response(HTTPStatus.INTERNAL_SERVER_ERROR)
            self.end_headers()
            raise
        else:
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(result), "utf-8"))

    def log_message(self, *args, **kwargs):
        pass


class Server:
    def __getattr__(self, item):
        def f(**kwargs):
            if IS_SERVER:
                return PATHS["/" + item](**kwargs)
            else:
                return multiplayer_post(item, kwargs)

        return f


Server = Server()


def multiplayer_post(path, data, server_url=None):
    """Post DATA to a multiplayer server PATH and return the response."""
    if not server_url:
        server_url = DEFAULT_SERVER
    data_bytes = bytes(json.dumps(data), encoding="utf-8")
    request = Request(server_url + "/" + path, data_bytes, method="POST")
    try:
        response = urlopen(request, context=ssl._create_unverified_context())
        text = response.read().decode("utf-8")
        if text.strip():
            return json.loads(text)
    except Exception as e:
        traceback.print_exc()
        print(e)
        return None


def multiplayer_route(path, server_path=None):
    """Convert a function that takes (data, send) into a route."""
    if not server_path:
        server_path = path

    def wrap(f):
        def send(data):
            return multiplayer_post(server_path, data)

        def routed_fn(data):
            response = f(data, send)
            return response

        route(path)(routed_fn)
        return f

    return wrap


@path_optional
def forward_to_server(path):
    def wrap(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if IS_SERVER:
                return f(*args, **kwargs)
            else:
                return multiplayer_post(path, kwargs)

        return wrapped

    return wrap


def server_only(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if IS_SERVER:
            return f(*args, **kwargs)
        else:
            raise Exception("Method not available locally!")

    return wrapped


def sendto(f):
    def wrapped(data):
        return f(**data)

    return wrapped


def start_server():
    global IS_SERVER
    IS_SERVER = True
    from flask import Flask, request, jsonify, send_from_directory, Response

    app = Flask(__name__, static_url_path="", static_folder="")
    for route, handler in PATHS.items():

        def wrapped_handler(handler=handler):
            return jsonify(handler(**snakify(request.get_json(force=True))))

        app.add_url_rule(route, handler.__name__, wrapped_handler, methods=["POST"])

    for route, handler in STATIC_PATHS.items():

        def wrapped_handler(route=route, handler=handler):
            query_params = parse_qs(request.query_string.decode())
            return Response(
                handler(**snakify(query_params)),
                mimetype=CONTENT_TYPE_LOOKUP[route.split(".")[-1]],
            )

        app.add_url_rule(
            route, handler.__name__ + route, wrapped_handler, methods=["GET"]
        )

    @app.route("/")
    def index():
        return send_from_directory("", "index.html")

    return app


def start_client(port, default_server, gui_folder, standalone):
    """Start web server."""
    global DEFAULT_SERVER, GUI_FOLDER, IS_SERVER
    DEFAULT_SERVER = default_server
    GUI_FOLDER = gui_folder
    IS_SERVER = False

    socketserver.TCPServer.allow_reuse_address = True
    httpd = HTTPServer(("localhost", port), Handler)
    if not standalone:
        webbrowser.open("http://localhost:" + str(port), new=0, autoraise=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.socket.close()


def snakify(data):
    out = {}
    for key, val in data.items():
        snake_key = []
        for x in key:
            if x != x.lower():
                snake_key += "_"
            snake_key += x.lower()
        out["".join(snake_key)] = val
    return out


@route("/kill")
def kill():
    if not IS_SERVER:
        print("Exiting GUI")
        exit(0)


def start(port, default_server, gui_folder, db_init=None):
    global DEFAULT_SERVER
    DEFAULT_SERVER = default_server

    parser = argparse.ArgumentParser(description="Project GUI Server")
    parser.add_argument(
        "-s", help="Stand-alone: do not open browser", action="store_true"
    )
    parser.add_argument("-f", help="Force Flask app", action="store_true")
    args, unknown = parser.parse_known_args()

    import __main__

    if "gunicorn" not in os.environ.get("SERVER_SOFTWARE", "") and not args.f:
        request = Request(
            "http://127.0.0.1:{}/kill".format(port),
            bytes(json.dumps({}), encoding="utf-8"),
            method="POST",
        )
        try:
            urlopen(request)
            print("Killing existing gui process...")
            time.sleep(1)
        except URLError:
            pass

        start_client(port, default_server, gui_folder, args.s)
    else:
        if db_init:
            db_init()
        app = start_server()
        if args.f:
            app.run(port=port, threaded=False, processes=1)
        else:
            return app
