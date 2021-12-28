# Python program to implement the Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(input_text, shift_key, direction_of_string):
    output_text = ""
    new_char_index = 0
    for letter in input_text:
        if letter not in alphabet:  # Special case for spaces, special characters (non-alphabets)
            output_text += letter  # Just append it to the output string as it is
            continue  # Continue looping with the next letter in the text string
        else:  # An alphabet
            char_index = alphabet.index(letter)  # Find the index of the current letter in the alphabet list
            if direction_of_string == 'encode':
                new_char_index = char_index + shift_key  # Calculate the new character to replace it with
                if new_char_index > 25:  # Special case to take care if index > 25 (eg. 'z')
                    new_char_index = new_char_index - 26  # Loop back to the beginning of the alphabet list
            elif direction_of_string == 'decode':
                new_char_index = char_index - shift_key  # Calculate the new character to replace it with
                if new_char_index < 0:  # Special case to take care if index < 0 (eg. 'a')
                    new_char_index = 26 + new_char_index  # Loop back to the end of the alphabet list

            output_text += alphabet[new_char_index]  # Append the new character to the output text

    print(f"The {direction_of_string.upper()}D text is: '{output_text}'")


continue_program = "yes"
while continue_program == 'yes':

    direction = ""
    while direction not in ['encode', 'decode']:
        direction = input("Type 'encode' to encrypt, 'decode' to decrypt: ").lower()

    # Taking user input and calling the encrypt/decrypt function based on user selection
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    # Call the caesar function to encode or decode based on user input
    caesar(text, shift, direction)

    continue_program = input("Do you want to continue? Type 'Yes' or 'No': ").lower()
