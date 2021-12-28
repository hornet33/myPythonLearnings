# Python program to simulate the hangman game
import os
import random
import hangman_art
import hangman_word_bank


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


# Initialize variables
end_of_game = False  # Boolean variable to check if end of game is reached
word_list = hangman_word_bank.word_list  # Accessing the word bank from the external Python module
stages = hangman_art.stages  # Accessing the ASCII art from the external Python module
chosen_word = random.choice(word_list).upper()  # Randomly selecting a word from the word list
chosen_word_length = len(chosen_word)  # Saving the length of the chosen word in a variable
lives = 6  # Variable to keep track of the number of lives left, set to 6
guessed_letters_list = []

display = []  # Creating a blank list for displaying the guessed letters to the user
for _ in range(chosen_word_length):  # Looping through the length of the chosen word and initializing the list to "_"
    display.append("_")

screen_clear()
# Displaying the hangman logo at the start
print(hangman_art.logo)

# Displaying the first blank display so that user knows how many letters are in the word to guess
print(f"\nYour word to guess: {' '.join(display)}")

while not end_of_game:  # Loop until end of game is not true

    guess = input("Guess a letter: ").upper()  # Taking user input

    screen_clear()  # Clear the screen
    # Displaying the hangman logo at the start
    print(hangman_art.logo)

    # Logic to ensure a new letter is guessed - if not, user is asked to enter letter again
    if guess in guessed_letters_list:  # Check the guessed letter in the list which stores all letters guessed so far
        print("Please choose a letter you have not guessed before.")
        continue  # Go back to the beginning of the while loop to guess another letter
    else:
        guessed_letters_list.append(guess)  # Valid guess, add to the list of already guessed letters for future guesses

    # Loop to check if the user input matches with a character in the chosen word
    for position in range(chosen_word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess  # If a match is found, display list is replaced with the actual word
            found = True

    if guess not in display:  # Wrong guess
        print("Wrong guess!")
        lives -= 1  # Reduce 1 life
        print(stages[lives])  # Display the hangman's status
        if lives == 0:  # If all lives are lost, then user loses
            print(f"You Lose! The right word was '{chosen_word}'.")
            end_of_game = True  # Set end of game to true to exit the while loop
            continue
    else:  # Let the user know the guess was right
        print("Right guess!")

    # Join all the elements in the list and turn it into a String.
    print(f"\nYour word to guess: {' '.join(display)}")  # Correct letters in the word are revealed to the user

    # Check if display has any blank ('_') - if no, end of game is reached
    if '_' not in display:
        end_of_game = True
        print("You win! Good job!")
