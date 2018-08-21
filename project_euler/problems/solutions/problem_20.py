from problems.solutions.problem_16 import sum_digits

problem_title = "Factorial digit sum"
problem_statement = (
    "n! means n × (n − 1) × ... × 3 × 2 × 1, For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, "
    "and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. "
    "Find the sum of the digits in the number 100!"
)


def solve(num=100):
    total = 1
    for i in range(2, num + 1):
        total *= i

    return sum_digits(total)
