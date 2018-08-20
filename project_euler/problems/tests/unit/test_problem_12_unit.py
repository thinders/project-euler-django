from django.test import SimpleTestCase

from problems.solutions.problem_12 import solve, factors


class Problem12Tests(SimpleTestCase):
    def test_factors(self):
        self.assertEqual({1, 2, 4, 7, 14, 28}, factors(28))

    def test_solve(self):
        self.assertEqual(28, solve(5))

    def test_solve_problem(self):
        self.assertEqual(76576500, solve())
