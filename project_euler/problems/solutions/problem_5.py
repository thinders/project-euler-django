problem_title = "Smallest multiple"
problem_statement = (
    "2520 is the smallest number that can be divided by each of the numbers from 1 to 10 "
    "without any remainder. What is the smallest positive number that is evenly divisible "
    "by all of the numbers from 1 to 20?"
)


def solve(num=20):
    smallest_multiple = num * (num - 1)
    current = smallest_multiple

    while True:
        for i in range(num, 1, -1):
            if current % i != 0:
                current += smallest_multiple
                break
            if i == 2:
                return current
