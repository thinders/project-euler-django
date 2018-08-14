from math import sqrt

problem_title = "Largest prime factor"
problem_statement = (
    "The prime factors of 13195 are 5, 7, 13 and 29. What is the "
    "largest prime factor of the number 600851475143?"
)


def get_prime_numbers(num):
    max_num_idx = num + 1
    which_indexes_are_prime = [True] * max_num_idx

    which_indexes_are_prime[0] = False
    which_indexes_are_prime[1] = False
    for num in range(2, max_num_idx):
        if which_indexes_are_prime[num]:
            for non_prime in range(num * num, max_num_idx, num):
                which_indexes_are_prime[non_prime] = False
    return [i for i, x in enumerate(which_indexes_are_prime) if x]


def get_possible_prime_factors(num):
    return get_prime_numbers(int(sqrt(num)))


def solve(num=600851475143):
    prime_numbers = get_possible_prime_factors(num)

    largest_prime_factor = 1
    for prime in reversed(prime_numbers):
        if num % prime == 0:
            largest_prime_factor = prime
            break
    return largest_prime_factor
