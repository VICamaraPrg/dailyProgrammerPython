"""
Challenge #374 [Easy] Additive Persistence
"""


def sum_all_digits(n, result=0):  # Challenge + bonus
    if n == 0:
        return result
    else:
        return sum_all_digits(n // 10, result + n % 10)


def additive_persistence(n, steps=0):
    if n < 10:
        return steps
    else:
        return additive_persistence(sum_all_digits(n), steps + 1)


print(additive_persistence(13))
print(additive_persistence(1234))
print(additive_persistence(9876))
print(additive_persistence(199))
