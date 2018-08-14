from django.test import SimpleTestCase

from problems.solutions.problem_9 import solve


class Problem9Tests(SimpleTestCase):
    def test_solve(self):
        self.assertEqual(60, solve(12))

    def test_solve_problem(self):
        self.assertEqual(31875000, solve())
