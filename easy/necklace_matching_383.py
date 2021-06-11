"""
Challenge #383 [Easy] Necklace matching
"""

# Grab the last[-1], and make new string
# with last on 1st position + the rest EXCEPT the last[:-1].


def same_necklace(original, check):
    for i in range(len(original)):
        original = original[-1] + original[:-1]
        if original == check:
            return True, original, check
    return False


def repeats(necklace):
    ref = necklace
    repeat = 0
    for i in range(len(ref)):
        necklace = necklace[-1] + necklace[:-1]
        if necklace == ref:
            repeat += 1
    return repeat

