import random  # this module provides functions for generating random numbers.

play = "1"

while play == "1":
    # generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    for attempt in range(1, 4):
        guess = input(
            "Guess the number (between 1 and 10) in 3 attempts: ")
        if guess.isdigit():  # check if the input is a digit
            guess = int(guess)
            if guess == secret_number:
                print("\033[0;32m Congratulations! You guessed the number!")
                play = input(
                    "\033[1;5m               PLAY AGAIN?\n" "\033[0;32m (Press 1 to play again,\033[0;0m press any other key to quit): ")
                break  # exit the for loop if the player guessed correctly

            elif guess > secret_number:
                print("Try again with a lower number")
            elif guess < secret_number:
                print("Try again with a greater number")
        else:
            print("Please enter a number")
    else:
        print("\033[0;31mGame Over. The number was", secret_number)
        play = input(
            "\033[1;5m               PLAY AGAIN?\n" "\033[0;32m (Press 1 to play again,\033[0;0m press any other key to quit): ")
