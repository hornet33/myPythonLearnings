# Python program to generate a password based on user input
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Variable initialization
random_letters = ""
random_symbols = ""
random_numbers = ""
generated_easy_password = ""
generated_hard_password = ""

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for letter_rand in range(nr_letters):
    random_letters += random.choice(letters)

for symbol_rand in range(nr_symbols):
    random_symbols += random.choice(symbols)

for number_rand in range(nr_numbers):
    random_numbers += random.choice(numbers)

generated_easy_password = random_letters + random_symbols + random_numbers
print(f"Generated Easy Password: {generated_easy_password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Converting the generated_easy_password from a string to a list
easy_pwd_as_list = list(generated_easy_password)
# Using in-built random.shuffle(<list>) to shuffle the contents
random.shuffle(easy_pwd_as_list)
# Joining the shuffled list in generated_hard_password variable
for char in easy_pwd_as_list:
    generated_hard_password += char
print(f"Generated Hard Password: {generated_hard_password}")
