# Python capstone project to simulate a Blackjack game
# ############## Our Blackjack House Rules #####################

# # The deck is unlimited in size.
# # There are no jokers.
# # The Jack/Queen/King all count as 10.
# # The Ace can count as 11 or 1.
# # Use the following list as the deck of cards:
# # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# # The cards in the list have equal probability of being drawn.
# # Cards are not removed from the deck as they are drawn.
# # The computer is the dealer.

# #################### Hints #####################
# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

from helpers.utilities import screen_clear
from blackjack_art import logo
import random

# Globals
# Using a list to store the card values - Ace has a default value of 11 unless player score > 21, then Ace = 1
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
cards_length = len(cards)


def draw_card(player):
    """Function to draw a random card from the cards list, append to the user/computer list and return the card value"""
    random_card = cards[random.randint(0, cards_length - 1)]
    if player == 'user':
        user_cards.append(random_card)
    elif player == 'computer':
        computer_cards.append(random_card)
    # Return card value
    return random_card


def print_final_score(user_score, computer_score):
    """Function to print the final scores of user and computer, and to declare the result of the game"""
    print("")  # Print a blank line
    print("-----------------------")
    print("F I N A L   S C O R E S")
    print("-----------------------")
    print(f"You     : Final cards {user_cards} | Final score {user_score}")
    print(f"Computer: Final cards {computer_cards} | Final score {computer_score}")
    # Check scores
    if user_score > 21:  # User went bust - computer wins
        print("RESULT: You went bust - you lose!")
    elif computer_score > 21:  # Computer went bust - user wins
        print("RESULT: Computer went bust - you win!")
    elif computer_score == 21 and len(computer_cards) == 2:  # Computer got a blackjack - it wins
        print("RESULT: Computer got a BLACKJACK - you lose!")
    elif user_score == 21 and len(user_cards) == 2:  # User got a blackjack - he wins
        print("RESULT: You got a BLACKJACK - you win!")
    elif user_score == computer_score:  # It's a draw
        print("RESULT: It's a draw - nobody loses!")
    elif user_score > computer_score:  # User wins
        print("RESULT: You win")
    else:  # Computer wins
        print("RESULT: Computer wins!")
    print("")  # Print a blank line


def play_blackjack():
    """Function to play the game of Blackjack"""
    user_total = 0
    computer_total = 0
    user_cards.clear()  # Clearing the user_cards list for a new game
    computer_cards.clear()  # Clearing the computer_cards list for a new game

    # Logo and clear screen will go here
    screen_clear()
    print(logo)

    # First draw - 2 cards each
    for _ in range(2):
        user_total += draw_card("user")
        computer_total += draw_card("computer")

    # Display user's first draw cards + total, and computer's only first card
    print(f"Your cards are {user_cards} | Your current score is {user_total}")
    print(f"Computer's first card is {computer_cards[0]}")

    if user_total == 21 or computer_total == 21:  # Check if either user or computer has a blackjack
        print_final_score(user_total, computer_total)
    else:  # Continue normal game
        draw_more_cards = True
        while draw_more_cards and user_total < 22:
            user_choice_another_card = input("\nType 'y' to draw another card, type 'n' to pass: ").lower()
            if user_choice_another_card == 'y':
                # Draw another card
                user_total += draw_card("user")
                # Logic to check if user_total > 21 and if user has an Ace (value 11)
                if user_total > 21 and 11 in user_cards:
                    # Change Ace to 1
                    index_ace = user_cards.index(11)
                    user_cards[index_ace] = 1
                    # Recalculate user_total
                    user_total -= 10  # Subtract 11, add 1 = subtract 10
                # Print updated user cards after draw
                print(f"Your cards are now {user_cards} | Your current score is {user_total}")
                print(f"Computer's first card is {computer_cards[0]}")
            elif user_choice_another_card == 'n':
                draw_more_cards = False
                # Computer draws more cards now based on score <= 16
                while computer_total <= 16:
                    computer_total += draw_card("computer")
                # If computer total > 21 and if it has an Ace (value 11)
                if computer_total > 21 and 11 in computer_cards:
                    # Change Ace to 1
                    index_ace = computer_cards.index(11)
                    computer_cards[index_ace] = 1
                    # Recalculate computer_total
                    computer_total -= 10  # Subtract 11, add 1 = subtract 10
                elif computer_total >= 21:
                    break
        # Display final score
        print_final_score(user_total, computer_total)
    return


# Main loop
screen_clear()
play = True
while play:
    user_choice = input("Are you ready to play some Python Blackjack (Y/N)? ").lower()
    if user_choice == 'n':
        play = False
    else:
        play_blackjack()
