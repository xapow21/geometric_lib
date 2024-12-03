import unittest
import rectangle
import triangle
import circle
import square
import math
class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_negative_mul(self):
        self.assertFalse(rectangle.area(-5,10))
        
    def test_zero_per(self):
        res = rectangle.perimeter(10,0)
        self.assertEqual(res,20)

    def test_equal_per(self):
        res = rectangle.perimeter(10,10)
        self.assertEqual(res,40)

    def test_negative_per(self):
        res = rectangle.perimeter(-5,10)
        self.assertFalse(res)

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = triangle.area(10, 10)
        self.assertEqual(res, 50)

    def test_negative_mul(self):
        self.assertFalse(triangle.area(-5,10))
        
    def test_zero_per(self):
        res = triangle.perimeter(10,0,5)
        self.assertEqual(res,15)

    def test_equal_per(self):
        res = triangle.perimeter(10,10,10)
        self.assertEqual(res,30)

    def test_negative_per(self):
        res = triangle.perimeter(-5,10,10)
        self.assertFalse(res)

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_negative_mul(self):
        self.assertFalse(square.area(-5))
        
    def test_zero_per(self):
        res = square.perimeter(0)
        self.assertEqual(res,0)

    def test_equal_per(self):
        res = square.perimeter(10)
        self.assertEqual(res,40)

    def test_negative_per(self):
        res = square.perimeter(-5)
        self.assertFalse(res)

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = circle.area(10)
        self.assertEqual(res, math.pi*100)

    def test_negative_mul(self):
        self.assertFalse(circle.area(-5))
        
    def test_zero_per(self):
        res = circle.perimeter(0)
        self.assertEqual(res,0)

    def test_equal_per(self):
        res = circle.perimeter(10)
        self.assertEqual(res,20*math.pi)

    def test_negative_per(self):
        res = circle.perimeter(-5)
        self.assertFalse(res)
unittest.main()
