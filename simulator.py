from random import randint
import matplotlib.pyplot as pyplot
import sys


def dice_roll(max_num, num_rolls=1):
    results = []
    i = 0
    while i < num_rolls:
        turn = randint(1, max_num)
        i += 1
        results.append(turn)
    return results


def interactive(max_num):
    repeat = True

    while repeat:
        results = dice_roll(max_num)
        print("You rolled ", results[0])
        print("Do you want to roll again?")
        repeat = ("y" or "yes") in input().lower()


def plot_histogram(results, no_buckets):
    pyplot.hist(results, no_buckets, density=1, facecolor='g', alpha=0.75)
    pyplot.xlabel('Dice Number')
    pyplot.ylabel('Probability')
    pyplot.title('100 Dice Roles')
    pyplot.show()

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
                raise ValueError("Please make sure you submit a whole number e.g.: python %s 6 4" % args[0])
    else:
        max_dice = 9

    if num_rolls is None:
        interactive(max_dice)
    else:
        results = dice_roll(max_dice, num_rolls)
        print(results)
        plot_histogram(results, max_dice)


if __name__ == "__main__":
    main(sys.argv)
