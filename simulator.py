from random import randint
import sys


def main(args):
    if len(args) <= 1:
        max_dice = 9
    else:
        try:
            max_dice = int(args[1])
        except ValueError:
            raise ValueError("Please make sure you submit a whole number e.g.: python %s 6" % args[0])

    repeat = True

    while repeat:
        print("You rolled ", randint(1, max_dice))
        print("Do you want to roll again?")
        repeat = ("y" or "yes") in input().lower()


if __name__ == "__main__":
    main(sys.argv)
