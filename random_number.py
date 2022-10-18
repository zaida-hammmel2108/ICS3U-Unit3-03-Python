#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Oct 2022
# This program is a number choosing game

import random


def main():
    # this function checks if the number you chose matches the random number.
    random_number = random.randint(1, 9)

    # input
    user_number = int(input("Pick a number between 0-9: "))

    # process
    if user_number == random_number:
        # output
        print("You've guessed the right number!")
    else:
        # output
        print("You guessed incorrectly. The number was {0}.".format(random_number))

    print("")
    print("\nDone.")


if __name__ == "__main__":
    main()
