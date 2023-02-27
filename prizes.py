# This is the module for prizes for hard mode winners

import random

prize = [
    # Niereich & Shadym - Flashban
    "https://www.youtube.com/watch?v=PPTG5OIR7Io",

    # Sideral (Superstrobe Remix) · DJ Dextro
    "https://www.youtube.com/watch?v=lOYQ8U_Hd8E",

    # H! DUDE - Understand
    "https://www.youtube.com/watch?v=YKMK6Ky5MTU",

    # Shadym & Tximeleta - M.D.M.A
    "https://www.youtube.com/watch?v=1Upc0apVWxY",

    # Checkmate · ROBPM
    "https://www.youtube.com/watch?v=4w0Grz5WHg4",

    # Kurt Leon - Treibjagd (T78 Remix)
    "https://www.youtube.com/watch?v=m7jOoZdv5I0",

    # Niereich - SPACESHIP (Roentgen Limiter Remix)
    "https://www.youtube.com/watch?v=H3FfHNVybqM",

    # Gaga & Mateo! - Pleasure (ROBPM Remix)
    "https://www.youtube.com/watch?v=4UWjTpgKyyU",

    # Acid Kit, Sebastian Mora - Pegasus (Original Mix)
    "https://www.youtube.com/watch?v=NiOWpwKD4fA",

    # Chris Lehmann - Drive (Niereich & Shadym Remix)
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",

]


def winner():

    # Does a dice roll
    dice_roll = random.randint(1, 6)

    # 20% chance of a prize
    if dice_roll == 6:

        # Randomly selects one number out of 10 (videos)
        random_prize = random.randint(0, 9)

        print("\nYou won a prize. Enjoy!")

        # Selects the random_prize from the list 'prize'
        print(prize[random_prize])
    else:
        print("Thank you for playing.")
