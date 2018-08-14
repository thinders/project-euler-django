problem_title = "Special Pythagorean triplet"
problem_statement = (
    "A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, "
    "a**2 + b**2 = c**2 "
    "For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2. There exists exactly one Pythagorean "
    "triplet for which a + b + c = 1000. Find the product abc."
)


def solve(num=1000):
    limit = num - 2
    for a in range(1, limit):
        for b in range(a + 1, limit):
            c = num - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
