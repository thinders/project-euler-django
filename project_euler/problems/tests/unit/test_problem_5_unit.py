from django.test import SimpleTestCase

from problems.solutions.problem_5 import solve


class Problem5Tests(SimpleTestCase):
    def test_solve(self):
        self.assertEqual(2520, solve(10))

    def test_solve_problem(self):
        self.assertEqual(232792560, solve())
