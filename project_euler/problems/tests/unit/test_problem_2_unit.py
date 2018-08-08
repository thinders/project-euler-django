from django.test import SimpleTestCase

from problems.solutions import problem_2


class Problem2Tests(SimpleTestCase):
    def test_solve(self):
        self.assertEqual(44, problem_2.solve(90))

    def test_solve_problem(self):
        self.assertEqual(4613732, problem_2.solve())
