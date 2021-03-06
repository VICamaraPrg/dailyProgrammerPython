"""
Challenge #393 [Easy] Making change
"""

coins = (500, 100, 25, 10, 5, 1)


def change(to_give): # Challenge
    total_coins = 0
    coin_selector = 0

    while to_give > 0:
        coin = coins[coin_selector]
        if to_give - coin >= 0:
            to_give -= coin
            total_coins += 1
        else:
            coin_selector += 1

    return total_coins


print(change(156))
print(change(12))
print(change(468))
print(change(123456))
