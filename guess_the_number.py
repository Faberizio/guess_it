# Fabrizio's Number Guessing Game v1.0


import random  # this module provides functions for generating random numbers.
from hard_mode import hard  # this module raises the difficulty


print("Welcome to Fabrizio's Amazing Number Guessing Game (F.A.N.G.G.)!\n")

play = (input("Enter '1' for an easy game or enter '2' for the hard mode: "))


def easy():
    play = "1"
    while play == "1":

        # generate a random number between 1 and 10
        secret_number = random.randint(1, 10)
        for attempt in range(1, 4):
            guess = input(
                "Guess the number (between 1 and 10) in 3 attempts or less: ")

            # check if the input is a digit
            if guess.isdigit():

                guess = int(guess)

                if guess == secret_number:
                    print(
                        f"Congratulations! You guessed the secret number '{secret_number}' \n")
                    play = input(
                        "Wanna play again? (1 for yes, any other key to quit): ")

                    # exit the for loop if the player guessed correctly
                    break

                elif guess > secret_number:
                    print("Try again with a lower number")

                elif guess < secret_number:
                    print("Try again with a greater number")
            else:
                print("Please enter a number")
        else:
            print(f"Game Over. The secret number was {secret_number}.")

            play = input(
                "Wanna play again? (1 for yes, any other key to quit): ")


if play == "1":
    easy()
elif play == "2":
    hard()
