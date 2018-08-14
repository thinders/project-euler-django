from problems.solutions.problem_3 import get_prime_numbers

problem_title = "10001st prime"
problem_statement = (
    "By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, "
    "we can see that the 6th prime is 13. What is the 10001st prime number?"
)


def solve(num=10001):
    primes = get_prime_numbers(1000000)
    return primes[num - 1]
