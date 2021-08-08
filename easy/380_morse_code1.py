"""
Challenge #380 [Easy] Smooshed Morse Code 1
"""

import itertools
import re
import string

with open('../test_inputs/en1list.txt') as f:
    words = f.read().splitlines()

morse = {}
alphabet = string.ascii_lowercase

with open('../test_inputs/morse_codes.txt') as f:
    codes = f.read().split()
    for idx, letter in enumerate(alphabet):
        morse[letter] = codes[idx]


def smorse(code, result=''):
    for letter in code:
        result += morse[letter]

    return result


def bonus1():
    frequencies = {}
    for word in words:
        code = smorse(word)
        if code not in frequencies:
            frequencies[code] = 0
        frequencies[code] += 1

    max_val = max(frequencies.values())
    max_key = [key for key, value in frequencies.items() if value == max_val]

    print(max_key, max_val)


def bonus2():
    for word in words:
        code = smorse(word)
        dots = re.search(r'(-)\1{14,}', code)
        if dots:
            print(code, word)


def bonus3():
    reduced_list = [w for w in words if w != 'counterdemonstrations' and len(w) == 21]
    for word in reduced_list:
        frequencies = {}
        code = smorse(word)
        for sign in code:
            if sign not in frequencies:
                frequencies[sign] = 0
            frequencies[sign] += 1
        if len(set(frequencies.values())) <= 1:  # Code from challenge #372 [Easy]
            print(word, frequencies)


def bonus4():
    reduced_list = [w for w in words if len(w) == 13]
    for word in reduced_list:
        code = smorse(word)
        if code == code[::-1]:
            print(code, word)


def bonus5():  # Here I notice that I could had the coded dictionary from the beginning.
    # Will change it on other version.
    with open('../test_inputs/en1list.txt') as f:
        coded = {word: smorse(word) for word in f.read().splitlines()}

    reduced_list = ' '.join([w for w in words if len(w) >= 13])
    possible_seq = [''.join(seq) for seq in itertools.product('.-', repeat=13) if ''.join(seq) not in reduced_list]
    possible_seq.remove('--.---.---.--')

    for x in coded.values():
        if len(x) >= len('--.---.---.--'):
            for y in possible_seq:
                if y in x:
                    possible_seq.remove(y)
    print(possible_seq)


bonus1()
bonus2()
bonus3()
bonus4()
bonus5()
