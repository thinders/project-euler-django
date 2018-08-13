from django.test import SimpleTestCase

from problems.solutions.problem_4 import solve, is_palindrome


class Problem4Tests(SimpleTestCase):
    def test_is_palindrome_with_even_digits(self):
        self.assertTrue(is_palindrome(9009))

    def test_is_palindrome_with_odd_digits(self):
        self.assertTrue(is_palindrome(90609))

    def test_not_is_palindrome(self):
        self.assertFalse(is_palindrome(956459))

    def test_not_is_palindrome_with_odd_digits(self):
        self.assertFalse(is_palindrome(90608))

    def test_solve_problem(self):
        self.assertEqual(906609, solve())
