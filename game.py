import random

exit = "e"
user_points = 0
computer_points = 0
while True:
    options = ["rock", "paper", "scissors"]
    user_input = input ("Choose rock, paper, scissors, e for exit:  ") 
    computer_input = random.choice(options)

    if user_input == exit:
        print("Game over")
        print(f"Your total score is {user_points} and total computer points is {computer_points}")
        break

    if user_input == "rock":
        if computer_input == "rock":
            print("You chose rock")
            print("computer chose rock")
            print("There is no winner")

        elif computer_input == "paper":
            print("You chose rock")
            print("computer chose paper")
            print("Computer wins")
            computer_points += 1

        elif computer_input == "scissors":
            print("You chose rock")
            print("computer chose scissors")
            print("You win")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "paper":
            print("You chose paper")
            print("computer chose paper")
            print("There is no winner")

        elif computer_input == "scissors":
            print("You chose paper")
            print("computer chose scissors")
            print("Computer wins")
            computer_points += 1

        elif computer_input == "rock":
            print("You chose paper")
            print("computer chose rock")
            print("You win")
            user_points += 1

    elif user_input == "scissors":
        if computer_input == "scissors":
            print("You chose scissors")
            print("computer chose scissors")
            print("There is no winner")

        elif computer_input == "rock":
            print("You chose scissors")
            print("computer chose rock")
            print("Computer wins")
            computer_points += 1

        elif computer_input == "paper":
            print("You chose scissors")
            print("computer chose paper")
            print("You win")
            user_points += 1

    #elif user_input != "rock" or user_input != "paper" or user_input != "scissors" or user_input != "exit":
    else:
        print("invalid input. Please select from the options provided")