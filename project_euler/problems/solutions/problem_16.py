problem_title = "Power digit sum"
problem_statement = (
    "2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26. "
    "What is the sum of the digits of the number 21000?"
)


def sum_digits(mul):
    total = 0
    for x in str(mul):
        total += int(x)
    return total


def solve(num=1000):
    mul = 2
    for i in range(1, num):
        mul *= 2

    return sum_digits(mul)
