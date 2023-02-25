# Fabrizio's Number Guessing Game v1.1
# This is the hard mode module
# Result don't give any hints but there are prizes to be won


import random  # this module provides functions for generating random numbers.
from prizes import winner


def hard():
    print("\nWelcome to the Hard mode! No hints this time!!")
    play = "2"

    while play == "2":

        # generate a random number between 1 and 10
        secret_number = random.randint(1, 10)

        for attempt in range(1, 4):
            guess = input(
                "Guess the number (between 1 and 10) in 3 attempts or less: ")

            # check if the input is a digit.
            if guess.isdigit():

                guess = int(guess)

                if guess == secret_number:
                    print(
                        f"Amazing! You guessed the secret number '{secret_number}' on hard mode!")

                    # calls function winner() from module "prizes"
                    winner()

                    play = input(
                        "Wanna play again? (Enter '2' for another round of hard mode, or any other key to quit): ")

                    # exit the for loop if the player guessed correctly
                    break

                elif guess != secret_number:
                    print("Nope. Guess again...")

            else:
                print("Please enter a number")
        else:
            print(f"Game Over. The secret number was {secret_number}.")
            play = input(
                "Wanna play again? (Enter '2' for another round of hard mode, or any other key to quit): ")
