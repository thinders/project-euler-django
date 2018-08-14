from django.test import SimpleTestCase

from problems.solutions.problem_14 import solve, number_of_terms_in_chain


class Problem14Tests(SimpleTestCase):
    def test_number_of_terms_in_chain(self):
        self.assertEqual(10, number_of_terms_in_chain(13))

    def test_solve(self):
        self.assertEqual(837799, solve())
