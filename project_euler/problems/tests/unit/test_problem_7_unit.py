from django.test import SimpleTestCase

from problems.solutions.problem_7 import solve


class Problem7Tests(SimpleTestCase):
    def test_solve(self):
        self.assertEqual(13, solve(6))

    def test_solve_problem(self):
        self.assertEqual(104743, solve())
