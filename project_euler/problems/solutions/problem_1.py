

def solve():
    MAX_NUMBER = 1000
    total = 0
    for x in range(5, MAX_NUMBER, 5):
        total += x
    for x in range(3, MAX_NUMBER, 3):
        if x % 5 != 0:
            total += x

    return total