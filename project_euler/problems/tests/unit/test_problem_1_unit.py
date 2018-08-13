from django.test import SimpleTestCase

from problems.solutions.problem_1 import solve


class Problem1Tests(SimpleTestCase):
    def test_solve(self):
        self.assertEqual(23, solve(10))

    def test_solve_with_1000(self):
        self.assertEqual(233168, solve())
