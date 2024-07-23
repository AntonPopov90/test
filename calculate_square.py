from math import pi, sqrt
import unittest


def circle_square(radius:int or float)->float: # type: ignore
    """calculate circle square"""
    return pi * radius**2


def triangle_square(side_1:int or float, side_2:int or float, side_3:int or float)->float: # type: ignore
    """calculate triangle square"""
    triangle_square = (side_1 + side_2 + side_3) / 2
    square = sqrt(triangle_square * (triangle_square - side_1) * (triangle_square - side_2) * (triangle_square - side_3))
    return square


def right_angled(a:int or float, b:int or float, c:int or float)->bool: # type: ignore
    """check right-angled triangle or not"""
    if (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b) :
        return True 
    else:
        return False


class TestGeometry(unittest.TestCase):


    def test_circle_area(self):
        """test circle_square func"""
        self.assertAlmostEqual(circle_square(5), 78.54, places=2)


    def test_triangle_area(self):
        """test triangle_square func"""
        self.assertAlmostEqual(triangle_square(3, 4, 5), 6)


    def test_is_right_triangle(self):
        """check right_angled func"""
        self.assertTrue(right_angled(3, 4, 5))
        self.assertFalse(right_angled(5, 6, 7))
