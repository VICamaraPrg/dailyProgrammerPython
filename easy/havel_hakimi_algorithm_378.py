"""
Challenge #378 [Easy] Havel-Hakimi Algorithm
"""


def remove_zeros(l):
    return [n for n in l if n != 0]


def desc_sort(l):
    l.sort()
    return l[::-1]


def len_check(n, l):
    return n > len(l)


def front_elimination(n, l):
    for x in range(n):
        l[x] -= 1
    return l


def havel_hakimi(l):
    while True:
        l = remove_zeros(l)
        if not l:
            return True
        l = desc_sort(l)
        n = l.pop(0)
        if len_check(n, l):
            return False
        l = front_elimination(n, l)

print(havel_hakimi([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]))
print(havel_hakimi([4, 2, 0, 1, 5, 0]))
print(havel_hakimi([3, 1, 2, 3, 1, 0]))
print(havel_hakimi([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]))
print(havel_hakimi([1, 1]))
print(havel_hakimi([1]))
