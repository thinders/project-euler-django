problem_title = "Sum square difference"
problem_statement = (
    "The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385. "
    "The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 552 = 3025. "
    "Hence the difference between the sum of the squares of the first ten natural numbers and the "
    "square of the sum is 3025 − 385 = 2640. Find the difference between the sum of the squares of "
    "the first one hundred natural numbers and the square of the sum."
)


def solve(num=100):
    sum_of_squares = 0
    square_of_sums = 0

    for i in range(1, num + 1):
        sum_of_squares += i * i
        square_of_sums += i

    return (square_of_sums * square_of_sums) - sum_of_squares
