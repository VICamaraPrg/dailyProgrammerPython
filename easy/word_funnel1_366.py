"""
Challenge #366 [Easy] Word Funnel 1
"""

with open('../test_inputs/en1list.txt') as f:
    words = f.read().splitlines()


def funnel(s1, s2):
    for idx in range(len(s1)):
        if s1[:idx] + s1[idx + 1:] == s2:
            return True
    return False



def bonus1(s1):
    out = []
    for idx in range(len(s1)):
        word = s1[:idx] + s1[idx + 1:]
        if word in words:
            out.append(word)
    return set(out)

# Missing bonus 2 for the moment.


print(bonus1('boats'))
