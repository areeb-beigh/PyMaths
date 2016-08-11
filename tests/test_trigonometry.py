import unittest
import math

from src.trigonometry import calculate


class TrigonometryTestCase(unittest.TestCase):
    def setUp(self):
        self.sin_angles = [(180, 0.0), (90, 1.0), (45, 1/math.sqrt(2)), (60, math.sqrt(3)/2)]
        self.cos_angles = [(180, -1.0), (90, 0.0), (45, 1/math.sqrt(2)), (60, 1/2)]
        self.tan_angles = [(180, 0.0), (45, 1), (60, math.sqrt(3))]

    def test_sin(self):
        for angle_tuple in self.sin_angles:
            self.assertAlmostEqual(calculate("sin", angle_tuple[0], "degree"), angle_tuple[1])
            self.assertAlmostEqual(calculate("sin", math.radians(angle_tuple[0]), "radian"), angle_tuple[1])

    def test_cos(self):
        for angle_tuple in self.cos_angles:
            self.assertAlmostEqual(calculate("cos", angle_tuple[0], "degree"), angle_tuple[1])
            self.assertAlmostEqual(calculate("cos", math.radians(angle_tuple[0]), "radian"), angle_tuple[1])

    def test_tan(self):
        for angle_tuple in self.tan_angles:
            self.assertAlmostEqual(calculate("tan", angle_tuple[0], "degree"), angle_tuple[1])
            self.assertAlmostEqual(calculate("tan", math.radians(angle_tuple[0]), "radian"), angle_tuple[1])

    def test_asin(self):
        self.assertEqual(calculate("asin", 10, "degree"), math.asin(math.radians(10)))
        self.assertEqual(calculate("asin", 1, "radian"), math.asin(1))

    def test_acos(self):
        self.assertEqual(calculate("acos", 10, "degree"), math.acos(math.radians(10)))
        self.assertEqual(calculate("acos", 1, "radian"), math.acos(1))

    def test_atan(self):
        self.assertEqual(calculate("atan", 10, "degree"), math.atan(math.radians(10)))
        self.assertEqual(calculate("atan", 1, "radian"), math.atan(1))

    def test_sinh(self):
        self.assertEqual(calculate("sinh", 10, "degree"), math.sinh(math.radians(10)))
        self.assertEqual(calculate("sinh", 90, "radian"), math.sinh(90))

    def test_cosh(self):
        self.assertEqual(calculate("cosh", 10, "degree"), math.cosh(math.radians(10)))
        self.assertEqual(calculate("cosh", 90, "radian"), math.cosh(90))

    def test_tanh(self):
        self.assertEqual(calculate("tanh", 10, "degree"), math.tanh(math.radians(10)))
        self.assertEqual(calculate("tanh", 90, "radian"), math.tanh(90))

if __name__ == '__main__':
    unittest.main()
