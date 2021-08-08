"""
Challenge #383 [Easy] Necklace matching
"""

# Grab the last[-1], and make new string
# with last on 1st position + the rest EXCEPT the last[:-1].


def same_necklace(original, check): # Challenge
    reference = original
    for i in range(len(original)):
        original = original[-1] + original[:-1]
        if original == check:
            return True, reference, check
    return False, reference, check


def repeats(necklace):  # Bonus 1
    reference = necklace
    repeat = 0
    for i in range(len(reference)):
        necklace = necklace[-1] + necklace[:-1]
        if necklace == reference:
            repeat += 1
    return repeat


print(same_necklace('nicole', 'coleni'))
print(same_necklace('nicole', 'lenico'))
print(same_necklace('nicole', 'coneli'))
print(same_necklace('x', 'xx'))
print(same_necklace('xxxyy', 'xxyyy'))

print(repeats('abc'))
print(repeats('abcabcabc'))
print(repeats('lala'))
print(repeats(''))
