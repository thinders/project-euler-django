problem_title = "Longest Collatz sequence"
problem_statement = (
    "The following iterative sequence is defined for the set of positive integers: "
    "n → n/2 (n is even) "
    "n → 3n + 1 (n is odd) "
    "Using the rule above and starting with 13, we generate the following sequence: "
    "13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 "
    "It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. "
    "Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1. "
    "Which starting number, under one million, produces the longest chain? "
    "NOTE: Once the chain starts the terms are allowed to go above one million."
)

COUNTS_BY_NUMBER = {}


def number_of_terms_in_chain(num):
    x = num
    count = 1
    while x > 1:
        if x in COUNTS_BY_NUMBER:
            count += COUNTS_BY_NUMBER[x]
            break
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        count += 1

    COUNTS_BY_NUMBER[num] = count
    return count


def solve():
    most_terms = 0
    largest_num = 0
    for i in range(999999, 1, -1):
        cur_terms = number_of_terms_in_chain(i)
        if cur_terms > most_terms:
            most_terms = cur_terms
            largest_num = i

    return largest_num
