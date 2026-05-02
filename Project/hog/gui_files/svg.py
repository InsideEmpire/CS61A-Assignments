class SVGRect:
    def __init__(self, x, y, width, height, stroke, fill):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.stroke = stroke
        self.fill = fill

    def __str__(self):
        return """<rect x="{0}" y="{1}" width="{2}" height="{3}" stroke="{4}" fill="{5}" />""".format(
            self.x, self.y, self.width, self.height, self.stroke, self.fill
        )


class SVGCircle:
    def __init__(self, x, y, radius, stroke, fill):
        self.x = x
        self.y = y
        self.radius = radius
        self.stroke = stroke
        self.fill = fill

    def __str__(self):
        return (
            """<circle cx="{0}" cy="{1}" r="{2}" stroke="{3}" fill="{4}" />""".format(
                self.x, self.y, self.radius, self.stroke, self.fill
            )
        )


class SVGLine:
    def __init__(self, x1, y1, x2, y2, stroke):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.stroke = stroke

    def __str__(self):
        return """<line x1="{0}" y1="{1}" x2="{2}" y2="{3}" stroke="{4}" />""".format(
            self.x1, self.y1, self.x2, self.y2, self.stroke
        )


class SVGPolygon:
    def __init__(self, points, stroke, fill):
        self.points = points  # list of lists
        self.stroke = stroke
        self.fill = fill

    def __str__(self):
        points_str = " ".join(",".join(map(str, point)) for point in self.points)
        return """<polygon points="{0}" stroke="{1}" fill="{2}"/>""".format(
            points_str, self.stroke, self.fill
        )


class SVGText:
    def __init__(self, x, y, text, stroke, fill, font_size, font_family):
        self.x = x
        self.y = y
        self.text = text
        self.stroke = stroke
        self.fill = fill
        self.font_size = font_size
        self.font_family = font_family

    def __str__(self):
        return """<text x="{0}" y="{1}" stroke="{2}" fill="{3}" font-size="{4}" font-family="{5}">{6}</text>""".format(
            self.x,
            self.y,
            self.stroke,
            self.fill,
            self.font_size,
            self.font_family,
            self.text,
        )


class SVGGraphic:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.shapes = []

    def draw_rect(self, x, y, width, height, stroke, fill):
        self.shapes.append(SVGRect(x, y, width, height, stroke, fill))

    def draw_circle(self, x, y, radius, stroke, fill):
        self.shapes.append(SVGCircle(x, y, radius, stroke, fill))

    def draw_line(self, x1, y1, x2, y2, stroke):
        self.shapes.append(SVGLine(x1, y1, x2, y2, stroke))

    def draw_polygon(self, points, stroke, fill):
        self.shapes.append(SVGPolygon(points, stroke, fill))

    def write_text(self, x, y, text, stroke, fill, font_size, font_family):
        self.shapes.append(SVGText(x, y, text, stroke, fill, font_size, font_family))

    def __str__(self):
        shapes = "".join(str(shape) for shape in self.shapes)
        return """<svg width="{0}" height="{1}" xmlns="http://www.w3.org/2000/svg">{2}</svg>""".format(
            self.width, self.height, shapes
        )


def create_graphic(width, height):
    return SVGGraphic(width, height)


def draw_rect(graphic, x, y, width, height, stroke="black", fill="black"):
    graphic.draw_rect(x, y, width, height, stroke, fill)


def draw_circle(graphic, x, y, radius, stroke="black", fill="black"):
    graphic.draw_circle(x, y, radius, stroke, fill)


def draw_line(graphic, x1, y1, x2, y2, stroke="black"):
    graphic.draw_line(x1, y1, x2, y2, stroke)


def draw_triangle(graphic, x1, y1, x2, y2, x3, y3, stroke="black", fill="black"):
    graphic.draw_polygon([[x1, y1], [x2, y2], [x3, y3]], stroke, fill)


def write_text(
    graphic,
    x,
    y,
    text,
    stroke="black",
    fill="black",
    font_size="medium",
    font_family="serif",
):
    graphic.write_text(x, y, text, stroke, fill, font_size, font_family)
