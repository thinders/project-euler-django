problem_title = "Amicable numbers"
problem_statement = (
    "Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n). "
    "If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b "
    "are called amicable numbers. "
    "For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. "
    "The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220. "
    "Evaluate the sum of all the amicable numbers under 10000."
)

DIVISORS = {}
AMICABLES = []


def divisors(num):
    d = {x for i in range(2, int(num ** 0.5) + 1) if not num % i for x in [i, num // i]}
    d.add(1)
    return d


def solve(num=10000):
    for i in range(2, num):
        f = divisors(i)
        divisor_sum = sum(f)
        DIVISORS[i] = divisor_sum

        if divisor_sum in DIVISORS and DIVISORS[divisor_sum] == i and i != divisor_sum:
            AMICABLES.append(i)
            AMICABLES.append(divisor_sum)

    return sum(AMICABLES)
