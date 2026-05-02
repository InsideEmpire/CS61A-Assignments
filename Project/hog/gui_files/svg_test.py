import unittest

import gui_files.svg as svg


class TestSVG(unittest.TestCase):
    def assert_contains_str(self, str, substr):
        self.assertTrue(str.find(substr) > -1, "%s does not contain %s" % (str, substr))

    def test_create_graphic(self):
        graphic = svg.create_graphic(200, 300)
        self.assertEqual(
            str(graphic),
            """<svg width="200" height="300" xmlns="http://www.w3.org/2000/svg"></svg>""",
        )

    def test_draw_rect(self):
        graphic = svg.create_graphic(200, 300)
        svg.draw_rect(graphic, 10, 20, 30, 40)
        self.assert_contains_str(
            str(graphic),
            """<rect x="10" y="20" width="30" height="40" stroke="black" fill="black" />""",
        )

    def test_draw_circle(self):
        graphic = svg.create_graphic(200, 300)
        svg.draw_circle(graphic, 10, 20, 30)
        self.assert_contains_str(
            str(graphic),
            """<circle cx="10" cy="20" r="30" stroke="black" fill="black" />""",
        )

    def test_draw_line(self):
        graphic = svg.create_graphic(200, 300)
        svg.draw_line(graphic, 10, 20, 30, 40)
        self.assert_contains_str(
            str(graphic), """<line x1="10" y1="20" x2="30" y2="40" stroke="black" />"""
        )

    def test_draw_triangle(self):
        graphic = svg.create_graphic(200, 300)
        svg.draw_triangle(graphic, 10, 20, 15, 150, 150, 150)
        self.assert_contains_str(
            str(graphic),
            """<polygon points="10,20 15,150 150,150" stroke="black" fill="black"/>""",
        )

    def test_write_text(self):
        graphic = svg.create_graphic(200, 300)
        svg.write_text(graphic, 10, 20, "Turn over")
        self.assert_contains_str(
            str(graphic),
            """<text x="10" y="20" stroke="black" fill="black" font-size="medium" font-family="serif">Turn over</text>""",
        )

    def test_write_text_font(self):
        graphic = svg.create_graphic(200, 300)
        svg.write_text(
            graphic, 10, 20, "Turn over", font_size="20", font_family="sans-serif"
        )
        self.assert_contains_str(
            str(graphic),
            """<text x="10" y="20" stroke="black" fill="black" font-size="20" font-family="sans-serif">Turn over</text>""",
        )

    def test_stroke_fill(self):
        graphic = svg.create_graphic(200, 300)
        svg.draw_rect(graphic, 10, 20, 30, 40, "pink", "blue")
        self.assert_contains_str(
            str(graphic),
            """<rect x="10" y="20" width="30" height="40" stroke="pink" fill="blue" />""",
        )


if __name__ == "__main__":
    unittest.main()
