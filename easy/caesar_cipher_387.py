"""
Challenge #387 [Easy] Caesar cipher
"""

import string

lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase
special_chars = (' ', ',', '.', '-',
                 '_', '/', '\\', '\'',
                 '\"', '?', '¿', '!',
                 '¡', '@', '$', '%')


# Challenge + Bonus 1
def caesar(secret, steps):
    ciphered = ''
    for letter in secret:
        if letter in special_chars:
            ciphered += letter
            continue
        elif letter.islower():
            idx = lower_alphabet.find(letter)
            ciphered += lower_alphabet[(idx + steps) % 26]
        else:
            idx = upper_alphabet.find(letter)
            ciphered += upper_alphabet[(idx + steps) % 26]

    return ciphered


print(caesar("jgorevxumxgsskx", 20))
secret = "¡Hello! How is your day going, mate?"
coded = caesar(secret, 14)
print(coded)
print(caesar(coded, -14))  # Back to original
