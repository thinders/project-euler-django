from django.test import SimpleTestCase

from problems.solutions import problem_3
from problems.solutions.problem_3 import get_possible_prime_factors


class Problem3Tests(SimpleTestCase):
    def test_get_possible_prime_factors(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17], get_possible_prime_factors(345))

    def test_solve(self):
        self.assertEqual(29, problem_3.solve(13195))

    def test_solve_problem(self):
        self.assertEqual(6857, problem_3.solve())
