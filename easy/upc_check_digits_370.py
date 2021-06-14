"""
Challenge #370 [Easy] UPC check digits
"""

#  This versions is fully string free, only int is parsed.
#  I could not find a way to not use strings for the bonus
#  I keep it as it is for the moment
# 0.39 Seconds in total to generate 100000 check digits (and printing them) Version 2.


def upc(number):
    reference = number
    odd_sum = 0
    even_sum = 0
    while number != 0:
        odd_sum += number % 10
        number //= 10
        even_sum += number % 10
        number //= 10
    M = ((even_sum + (odd_sum * 3)) % 10)
    M -= 2 if M != 0 else 0

    return reference * 10 + M


numbers = []

with open('../test_inputs/upc.txt') as lines:
    for line in lines:
        split = line.split()
        for values in split:
            numbers.append(int(values))

for i in numbers:
    print(upc(i))
