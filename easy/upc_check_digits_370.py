"""
Challenge #370 [Easy] UPC check digits
"""

#  This versions is fully string free, only int is parsed.
#  I could not find a way to not use strings for the bonus
#  I keep it as it is for the moment


def upc(number):
    copy = number
    reference = number // 10  # Prepare it for the even sum.
    odd_sum = 0
    even_sum = 0
    while number != 0:
        odd = number % 10
        number //= 100
        odd_sum += odd

    odd_sum *= 3
    while reference != 0:
        even = reference % 10
        reference //= 100
        even_sum += even
    M = (even_sum + odd_sum) % 10
    if M != 0:
        M -= 2

    return copy * 10 + M

print(upc(408450083954))  # 0
print(upc(841057310368))  # 0
