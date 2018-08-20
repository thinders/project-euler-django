from django.test import SimpleTestCase

from problems.solutions.problem_16 import solve


class Problem16Tests(SimpleTestCase):
    def test_solve(self):
        self.assertEqual(26, solve(15))

    def test_solve_problem(self):
        self.assertEqual(1366, solve())
