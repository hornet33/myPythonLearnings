# Python program to simulate the Higher-Lower Game
from higher_lower_art import logo, versus
from higher_lower_data import data
from helpers.utilities import screen_clear, get_random_number


def display_options_to_user(option_a, option_b):
    """Function to print the two options randomly selected for the user"""
    # Storing the list item - a dictionary - for the first and second person
    first_person = data[option_a]
    second_person = data[option_b]
    # Printing the required info for the two choices to the user - option A vs option B
    print(f"A: {first_person['name']}, {first_person['description']}, from {first_person['country']}")
    print(versus)
    print(f"B: {second_person['name']}, {second_person['description']}, from {second_person['country']}")


def check_user_choice(user_selection, option_a, option_b):
    """Function to check if the user selection from option_a or option_b. Returns true if correct, else false"""
    # Getting the follower_count for the two options for result comparison
    num_a = data[option_a]["follower_count"]
    num_b = data[option_b]["follower_count"]
    # If user selected option A and A has more followers than B, return true
    if num_a > num_b and user_selection == 'a':
        return True
    # If user selected option B and B has more followers than A, return true
    elif num_b > num_a and user_selection == 'b':
        return True
    # Else return false - wrong choice
    else:
        return False


def display_logo():
    """Function to clear the console and print the game logo"""
    screen_clear()
    print(logo)


def play_higher_lower():
    """Function to play the higher-lower game"""
    user_score = 0  # Initialize user_score
    data_total_length = len(data)  # Store the total length of the data list
    game_in_play = True  # Flag to check if game keeps continuing
    list_data_used = []  # List to store the options used so that same option doesn't come again

    # Get the first option
    option_1 = get_random_number(0, data_total_length - 1)
    option_2 = option_1  # Initialize to option_1
    list_data_used.append(option_1)  # Add option 1 to the list of used data

    # Loop until game is in play
    while game_in_play:

        # Generate a random option 2 - it should not be same as option 1 and should not be in the list of used data
        while option_2 == option_1 or option_2 in list_data_used:
            option_2 = get_random_number(0, data_total_length - 1)
        list_data_used.append(option_2)  # Add option 2 to the list of used data

        display_options_to_user(option_1, option_2)
        print("")

        # Get user input
        user_choice = 'c'  # Initialize to an invalid value for entering the while loop
        while user_choice.lower() not in ['a', 'b']:
            user_choice = input("Who has more Instagram followers? Choose an option 'A' or 'B': ").lower()
            if user_choice.lower() not in ['a', 'b']:
                print("\nPlease enter a valid choice 'A' or 'B'.")

        # Check user choice is correct or not
        game_in_play = check_user_choice(user_choice, option_1, option_2)

        if game_in_play:  # User selected the right option
            user_score += 1  # Increase user score
            option_1 = option_2  # Set last option of previous choice as the first option of the next set of choices
            display_logo()  # Clear screen and display logo
            print(f"\nYou got it right! Your current score = {user_score} \n")
        else:
            display_logo()
            print(f"\nSorry, that's the wrong answer - game over! Your final score = {user_score}")


# Main
display_logo()
play_higher_lower()  # Invoke the game module
