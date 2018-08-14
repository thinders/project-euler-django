from django.test import SimpleTestCase

from problems.solutions.problem_13 import solve


class Problem13Tests(SimpleTestCase):
    def test_solve(self):
        self.assertEqual("5537376230", solve())
