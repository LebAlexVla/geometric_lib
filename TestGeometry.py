import unittest

from trapezoid import area as trapezoid_area
from trapezoid import perimeter as trapezoid_perimeter
from parallelogram import area as parallelogram_area
from parallelogram import perimeter as parallelogram_perimeter

class TrapezoidTestCase(unittest.TestCase):
    def test_pos_base(self):
        res = trapezoid_area(4, 6, 10)
        self.assertEqual(res, 50)
        res = trapezoid_perimeter(4, 6, 8, 12)
        self.assertEqual(res, 30)
    def test_zero_base(self):
        res = trapezoid_area(0, 5, 10)
        self.assertEqual(res, 0)
        res = trapezoid_perimeter(0, 5, 10, 5)
        self.assertEqual(res, 0)
    def test_neg_base(self):
        res = trapezoid_area(-2, 5, 10)
        self.assertEqual(res, 0)
        res = trapezoid_perimeter(-2, 5, 10, 5)
        self.assertEqual(res, 0)

class ParallelogramTestCase(unittest.TestCase):
    def test_pos_side(self):
        res = parallelogram_area(4, 6)
        self.assertEqual(res, 24)
        res = parallelogram_perimeter(4, 6)
        self.assertEqual(res, 20)
    def test_zero_side(self):
        res = parallelogram_area(0, 6)
        self.assertEqual(res, 0)
        res = parallelogram_perimeter(0, 6)
        self.assertEqual(res, 0)
    def test_neg_side(self):
        res = parallelogram_area(-4, 6)
        self.assertEqual(res, 0)
        res = parallelogram_perimeter(-4, 6)
        self.assertEqual(res, 0)