import random
import re


def create_dice_roll(inp):  # Challenge + bonus
    l = re.search(r'(\d+)d(\d+)', inp)
    score = 0
    rolls = int(l.group(1))
    sides = int(l.group(2))
    list_roll = []
    final_roll = {}

    for r in range(1, rolls + 1):
        roll = random.randint(1, sides)
        score += roll
        list_roll.append(roll)

    final_roll[score] = list_roll
    return final_roll


print(create_dice_roll('5d12'))
print(create_dice_roll('6d4'))
print(create_dice_roll('1d2'))
print(create_dice_roll('1d8'))
print(create_dice_roll('3d6'))
print(create_dice_roll('4d20'))
print(create_dice_roll('100d100'))
