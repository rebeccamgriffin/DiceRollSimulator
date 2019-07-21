from random import randint
import sys

if len(sys.argv) <= 1:
    max_dice = 9
else:
    try:
        max_dice = int(sys.argv[1])
    except ValueError:
        raise ValueError("Please make sure you submit a whole number e.g.: python %s 6" % sys.argv[0])

repeat = True

while repeat:
    print("You rolled ",randint(1, max_dice))
    print("Do you want to roll again?")
    repeat = ("y" or "yes") in input().lower()
