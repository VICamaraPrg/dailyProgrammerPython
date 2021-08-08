"""
Challenge #375 [Easy] Print a new number by adding one to each of its digit
"""


def print_new(number):
    multiplier = 1
    total = 0
    while number != 0:
        next_n = (number % 10 + 1)
        total += next_n * multiplier
        if next_n >= 10:
            multiplier *= 100
        else:
            multiplier *= 10

        number //= 10
    return total


print(print_new(999))
print(print_new(191913))
print(print_new(1234))
print(print_new(2991))
