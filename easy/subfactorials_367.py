import itertools


def subfactorial(inp):  # Bonus, shortest code as possible: for me, 9 lines (Including def and return)
    factors, total = [i for i in range(1, inp + 1)], 0
    for perm in itertools.permutations(factors):
        coincidences = 0
        for idx, n in enumerate(factors):
            if perm.index(n) != factors.index(n):
                coincidences += 1
        if coincidences == inp:
            total += 1
    return total


print(subfactorial(6))
print(subfactorial(9))
