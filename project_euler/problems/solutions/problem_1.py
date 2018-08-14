problem_title = "Multiples of 3 and 5"
problem_statement = (
    "If we list all the natural numbers below 10 that are multiples of 3 or 5, "
    "we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all "
    "the multiples of 3 or 5 below 1000."
)


def solve(num=1000):
    total = 0
    for x in range(5, num, 5):
        total += x
    for x in range(3, num, 3):
        if x % 5 != 0:
            total += x

    return total
