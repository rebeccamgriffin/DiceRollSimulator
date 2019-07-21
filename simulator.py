from random import randint
import sys


def dice_roll(max_num, num_rolls=1):
    i = 0
    while i < num_rolls:
        print("You rolled ", randint(1, max_num))
        i += 1


def interactive(max_num):
    repeat = True

    while repeat:
        dice_roll(max_num)
        print("Do you want to roll again?")
        repeat = ("y" or "yes") in input().lower()


def main(args):

    num_rolls = None

    if len(args) > 1:
        try:
            max_dice = int(args[1])
        except ValueError:
            raise ValueError("Please make sure you submit a whole number e.g.: python %s 6" % args[0])

        if len(args) > 2:
            try:
                num_rolls = int(args[2])
            except ValueError:
                raise ValueError("Please make sure you submit a whole number e.g.: python %s 6" % args[0])
    else:
        max_dice = 9

    if num_rolls is None:
        interactive(max_dice)
    else:
        dice_roll(max_dice, num_rolls)


if __name__ == "__main__":
    main(sys.argv)
