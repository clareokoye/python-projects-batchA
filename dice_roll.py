import random
def roll_dice():

    dice_drawing = {
        1:(
            "O"
        ),

        2:(
            "OO"
        ),

        3:(
            "OOO"
        ),

        4:(
            "OOOO"
        ),

        5:(
            "OOOOO"
        ),

        6:(
            "OOOOOO"
        )

    
    }

    roll = input("Want to roll the dice? (Yes/No):  ").lower()

    while roll == "yes":
        dice1 = random.randint (1, 6)
        dice2 = random.randint (1, 6)
        print(f"dice is rolled: {dice1} and {dice2}")
        print(dice_drawing[dice1])
        print(" ")
        print(dice_drawing[dice2])
        roll = input("Want to roll the dice again? (Yes/No): ").lower()

roll_dice()
