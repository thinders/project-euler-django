from django.test import SimpleTestCase

from problems.solutions.problem_6 import solve


class Problem6Tests(SimpleTestCase):
    def test_solve(self):
        self.assertEqual(2640, solve(10))

    def test_solve_problem(self):
        self.assertEqual(25164150, solve())
