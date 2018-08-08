from django.test import SimpleTestCase

from problems.solutions import problem_1


class Problem1Tests(SimpleTestCase):
    def test_solve(self):
        self.assertEqual(23, problem_1.solve(10))

    def test_solve_with_1000(self):
        self.assertEqual(233168, problem_1.solve())
