from problems.solutions.problem_3 import get_prime_numbers

problem_title = "Summation of primes"
problem_statement = "The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million."


def solve(num=2000000):
    return sum(get_prime_numbers(num))
