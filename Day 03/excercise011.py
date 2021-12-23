# Python program to take input from user on type of pizza and calculate the final bill based on user selection
print("Welcome to Python Pizzas")
print("========================")

pizza_size = input("What size pizza do you want? S, M, or L: ")
want_pepperoni = input("Do you want pepperoni? Y or N: ")
want_extra_cheese = input("Do you want extra cheese? Y or N: ")
bill_amount = 0

# Charge for pizza size
if pizza_size.upper() == 'L':
    bill_amount = 25
elif pizza_size.upper() == 'M':
    bill_amount = 20
else:  # size = S
    bill_amount = 15

# Charge for pepperoni
if want_pepperoni.upper() == 'Y':
    if pizza_size == 'S':
        bill_amount += 2
    else:
        bill_amount += 3

# Charge for extra cheese
if want_extra_cheese.upper() == 'Y':
    bill_amount += 1

# Print final bill
print(f"Your final bill is: ${bill_amount}")
