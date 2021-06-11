"""
Challenge #391 [Easy] The ABACABA sequence
"""

import string

ALPHABET = string.ascii_lowercase


def abacaba_iterative():  # Challenge
    sequence = ""
    for i in range(len(ALPHABET)):
        leter = ALPHABET[i]
        sequence += leter + sequence
        print(i + 1, sequence)


def abacaba_recursive(n):  # Bonus
    if n < 1:
        return ""

    s = abacaba_recursive(n - 1)
    return s + ALPHABET[n - 1] + s


print(abacaba_recursive(18))
# abacaba_iterative()
