from django.test import SimpleTestCase

from problems.solutions.problem_21 import solve


class Problem16Tests(SimpleTestCase):
    def test_solve(self):
        self.assertEqual(504, solve(300))

    def test_solve_problem(self):
        self.assertEqual(31626, solve())
