from django.test import SimpleTestCase

from problems.solutions.problem_10 import solve


class Problem10Tests(SimpleTestCase):
    def test_solve(self):
        self.assertEqual(17, solve(10))

    def test_solve_problem(self):
        self.assertEqual(142913828922, solve())
