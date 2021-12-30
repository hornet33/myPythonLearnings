# Python program to play the rock-paper-scissors game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Add the Ascii art into a list
game_art = [rock, paper, scissors]

# Take the user input
user_choice = int(input("Choose 1 for Rock, 2 for Paper, 3 for Scissors:\n"))

# Error handling for invalid user input
if user_choice > 3 or user_choice < 1:
    print("Invalid choice - You Lose!")
else:
    # Print the game art for user choice
    print("You Chose: \n" + game_art[user_choice - 1])

    # Randomly select for computer choice
    computer_choice = random.randint(1, 3)  # Randomly selecting between 1, 2, and 3
    print("Computer Chose: \n" + game_art[computer_choice - 1])

    # Checking for rules of the game
    # Rock wins against scissors.
    # Scissors win against paper.
    # Paper wins against rock.

    if user_choice == 1 and computer_choice == 3:  # User = Rock | Computer = Scissors
        print("\n YOU WIN!")
    elif user_choice == 3 and computer_choice == 2:  # User = Scissors | Computer = Paper
        print("\n YOU WIN!")
    elif user_choice == 2 and computer_choice == 1:  # User = Paper | Computer = Rock
        print("\n YOU WIN!")
    elif user_choice == computer_choice:
        print("\n IT'S A DRAW!")
    else:
        print("\n COMPUTER WINS!")
