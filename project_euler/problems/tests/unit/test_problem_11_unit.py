from django.test import SimpleTestCase

from problems.solutions.problem_11 import (
    solve,
    get_left_diagonal,
    get_right_diagonal,
    MAX_COL,
    MAX_ROW,
    get_down,
    get_right,
)


class Problem11Tests(SimpleTestCase):
    def test_get_left_diagonal_protects_col(self):
        self.assertIsNone(get_left_diagonal(0, 2))

    def test_get_left_diagonal_protects_row(self):
        self.assertIsNone(get_left_diagonal(MAX_ROW - 3, 3))

    def test_get_left_diagonal(self):
        self.assertEqual(24468444, get_left_diagonal(0, 3))

    def test_get_right_diagonal_protects_col(self):
        self.assertIsNone(get_right_diagonal(MAX_ROW - 3, 0))

    def test_get_right_diagonal_protects_row(self):
        self.assertIsNone(get_right_diagonal(0, MAX_COL - 3))

    def test_get_right_diagonal(self):
        self.assertEqual(279496, get_right_diagonal(0, 0))

    def test_get_down_protects_row(self):
        self.assertIsNone(get_down(MAX_ROW - 3, 0))

    def test_get_down(self):
        self.assertEqual(1651104, get_down(0, 0))

    def test_get_right_protects_col(self):
        self.assertIsNone(get_right(0, MAX_COL - 3))

    def test_get_right(self):
        self.assertEqual(34144, get_right(0, 0))

    def test_solve(self):
        self.assertEqual(70600674, solve())
