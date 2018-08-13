from django.test import SimpleTestCase

from problems.solutions.problem_2 import solve


class Problem2Tests(SimpleTestCase):
    def test_solve(self):
        self.assertEqual(44, solve(90))

    def test_solve_problem(self):
        self.assertEqual(4613732, solve())
