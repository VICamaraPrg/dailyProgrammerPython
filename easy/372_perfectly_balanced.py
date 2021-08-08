"""
Challenge #372 [Easy] Perfectly balanced
"""
import string


def generate_map(word):
    word_frequency = {}
    for letter in word:
        if letter not in word_frequency:
            word_frequency[letter] = 0
        word_frequency[letter] += 1
    return word_frequency


def is_perfectly_balanced(frequency):
    if len(set(frequency.values())) <= 1:
        return True
    return False


print(is_perfectly_balanced(generate_map('abccbaabccba')))  # 4a,4b,4c -> True
print(is_perfectly_balanced(generate_map('www')))  # 3w -> True
print(is_perfectly_balanced(generate_map(string.ascii_lowercase)))  # 1 of each -> True
print(is_perfectly_balanced(generate_map('xxxyyyzzzz')))  # 3x,3y,4z -> False
print(is_perfectly_balanced(generate_map('bob')))  # 2b,1o -> False
print(is_perfectly_balanced(generate_map('fifo')))  # 2f,1i,1o -> False
