from django.test import SimpleTestCase

from problems.solutions.problem_8 import solve


class Problem8Tests(SimpleTestCase):
    def test_solve(self):
        self.assertEqual(5832, solve(4))

    def test_solve_problem(self):
        self.assertEqual(None, solve())
