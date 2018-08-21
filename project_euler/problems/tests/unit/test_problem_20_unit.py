from django.test import SimpleTestCase

from problems.solutions.problem_20 import solve


class Problem16Tests(SimpleTestCase):
    def test_solve(self):
        self.assertEqual(27, solve(10))

    def test_solve_problem(self):
        self.assertEqual(648, solve())
