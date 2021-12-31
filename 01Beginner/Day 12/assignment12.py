# Python program to create a number guessing game

from number_game_art import logo
from helpers.utilities import screen_clear
import random

# Globals
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def get_attempts_for_user_level(selected_level):
    """Function that returns the number of attempts for a selected user level"""
    if selected_level == 'easy':
        return EASY_ATTEMPTS
    elif selected_level == 'hard':
        return HARD_ATTEMPTS


# Select a random number
def get_random_number():
    """Function to generate a random number between (1,100) and return it"""
    return random.randint(1, 100)


def number_game(total_attempts, answer):
    """Function that contains the logic to play the number guessing game for the attempts and answer parameters"""
    # Keep a flag to check if game should continue
    continue_game = True
    while continue_game:
        # Display the total number of attempts the user has left
        if total_attempts > 1:
            print(f"You have {total_attempts} attempts to guess the right number!\n")
        else:
            print("Last attempt to guess the right number!\n")

        # Ask user to choose a number
        guess = int(input("Make your guess: "))

        # Give hints to the user
        if guess < answer:  # Print too low
            print("Your guess is too low\n")
        elif guess > answer:  # Print too high
            print("Your guess is too high\n")
        elif guess == answer:  # Print success
            print(f"You guessed it right - the answer was {answer}!\n")
            continue_game = False

        # Reduce one attempt
        total_attempts -= 1
        # Check if attempts are exhausted
        if total_attempts == 0:
            continue_game = False

    if guess != answer:
        print(f"You've run out of guesses, you lose! The right answer was {answer}.")


# Main
# Clear the screen and display the logo
screen_clear()
print(logo)

# Print the message that number is selected
print("I'm thinking of a number between 1 and 100 - you need to guess the right number.\n")
answer_num = get_random_number()  # Generate the random number for the user to guess

# Ask the user what level of difficulty he needs - easy or hard
user_level = input("Select a difficulty - type 'easy' or 'hard' to choose: ").lower()
attempts = get_attempts_for_user_level(user_level)  # Attempts depend on user level selected

# Call the game function
number_game(attempts, answer_num)
