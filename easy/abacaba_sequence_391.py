"""
Challenge #391 [Easy] The ABACABA sequence
"""

import string

ALPHABET = string.ascii_lowercase


def abacaba_iterative():
    sequence = ""
    for i in range(len(ALPHABET)):
        leter = ALPHABET[i]
        sequence += leter + sequence
        print(i + 1, sequence)


def abacaba_recursive(n):
    if n < 1:
        return ""

    s = abacaba_recursive(n - 1)
    return s + ALPHABET[n - 1] + s

# print(abacaba_recursive(25))
# abacaba_iterative()
