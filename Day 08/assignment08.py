# Python program to implement the Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# Create a function called 'decrypt' that takes the encrypted text and shift as inputs.
def decrypt(encrypted_text, shift_key):
    text_lower = encrypted_text.lower()
    decrypted_text = ""
    for letter in text_lower:
        if letter not in alphabet:  # Special case for spaces, special characters (non-alphabets)
            decrypted_text += letter  # Just append it to the encrypted string as it is
            continue  # Continue looping with the next letter in the text string
        else:  # An alphabet
            char_index = alphabet.index(letter)  # Find the index of the current letter in the alphabet list
            new_char_index = char_index - shift_key  # Calculate the new character to replace it with
            if new_char_index < 0:  # Special case to take care if index < 0 (eg. 'a')
                new_char_index = 26 + new_char_index  # Loop back to the beginning of the alphabet
            decrypted_text += alphabet[new_char_index]  # Append the new character to the encrypted text

    print(f"The decrypted text is '{decrypted_text}'")


# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(original_text, shift_key):
    text_lower = original_text.lower()  # Converting original text to all lowercase letters
    encrypted_text = ""  # Variable to store the final encrypted text, initialized to a blank string
    for letter in text_lower:  # Loop for every character in the text string
        if letter not in alphabet:  # Special case for spaces, special characters (non-alphabets)
            encrypted_text += letter  # Just append it to the encrypted string as it is
            continue  # Continue looping with the next letter in the text string
        else:  # An alphabet
            char_index = alphabet.index(letter)  # Find the index of the current letter in the alphabet list
            new_char_index = char_index + shift_key  # Calculate the new character to replace it with
            if new_char_index > 25:  # Special case to take care if index > 25 (eg. 'z')
                new_char_index = new_char_index - 26  # Loop back to the beginning of the alphabet
            encrypted_text += alphabet[new_char_index]  # Append the new character to the encrypted text

    print(f"The encrypted text is '{encrypted_text}'")


continue_program = True
while continue_program:

    direction = ""
    while direction not in ['encode', 'decode']:
        direction = input("Type 'encode' to encrypt, 'decode' to decrypt:\n")

    # Taking user input and calling the encrypt/decrypt function based on user selection
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction.lower() == 'encode':
        encrypt(original_text=text, shift_key=shift)
    elif direction.lower() == 'decode':
        decrypt(encrypted_text=text, shift_key=shift)

    another_round = input("Do you want to continue? Type 'Yes' or 'No': ")
    if another_round.lower() == 'yes':
        continue_program = True
    else:
        continue_program = False
