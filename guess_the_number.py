# Fabrizio's Number Guessing Game v1.0

import random  # this module provides functions for generating random numbers.
import time  # this module provides time related functions.
from hard_mode import hard  # this module raises the difficulty


print("Welcome to Fabrizio's Amazing Number Guessing Game (F.A.N.G.G.)!\n")

play = (input("Enter '1' for an easy game or enter '2' for the hard mode: "))


def easy():
    play = "1"

    while play == "1":

        # generate a random number between 1 and 10
        secret_number = random.randint(1, 10)
        for attempt in range(1, 4):

            st = time.time()  # gathers start time

            guess = input(
                "Guess the number (between 1 and 10) in 3 attempts: ")

            # check if the input is a digit
            if guess.isdigit():

                guess = int(guess)

                if guess == secret_number:
                    print(
                        f"\033[0;32mYou guessed the secret number '{secret_number}' \n")
                    etw = time.time()  # gathers end time for a winning attempt
                    elapsed_time = etw - st  # calculates elapsed time
                    print("Elapsed time: ", time.strftime(
                        "%H:%M:%S", time.gmtime(elapsed_time)))  # Prints elapsed time in a readable format
                    play = input(
                        "\033[1;5m               PLAY AGAIN?\n" "\033[0;32m (Press 1 to play again,\033[0;0m press any other key to quit): ")
                    break  # exit the for loop if the player guessed correctly

                elif guess > secret_number:
                    print("Try again with a smaller number.")

                elif guess < secret_number:
                    print("Try again with a greater number.")
            else:
                print("Please enter a number: ")
        else:
            et = time.time()  # gathers end time for a losing attempt
            elapsed_time_l = et - st  # calculates elapsed time
            print(
                f"\033[0;31mGame Over. The secret number was {secret_number}.")
            print("Elapsed time: ", time.strftime(
                "%H:%M:%S", time.gmtime(elapsed_time_l)))  # Prints elapsed time in a readable format
            play = input(
                "\033[1;5m               PLAY AGAIN?\n" "\033[0;32m (Press 1 to play again,\033[0;0m press any other key to quit): ")


if play == "1":
    easy()
elif play == "2":
    hard()

"""
ANSI color codes

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"    
"""
