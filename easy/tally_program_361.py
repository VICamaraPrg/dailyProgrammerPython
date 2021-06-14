"""
Challenge #361 [Easy] Tally Program
"""

def get_scores(line):
    scores = {char.lower(): 0 for char in line}

    for char in line:
        if char.isupper():
            scores[char.lower()] -= 1
        elif char.islower():
            scores[char.lower()] += 1
    return sorted(scores.items(), key=lambda x: (-x[1], x[0]))


print(get_scores('abcde'))
print(get_scores('dbbaCEDbdAacCEAadcB'))
print(get_scores('EbAAdbBEaBaaBBdAccbeebaec'))

