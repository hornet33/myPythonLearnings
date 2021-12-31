# Debugging the odd-even program

# --- Original program below ---
# number = int(input("Which number do you want to check?"))
# if number % 2 = 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# --- Corrected program below ---
number = int(input("Which number do you want to check?"))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# -- Explanation below ---
# Corrected the if condition; changed the assignment operator('=') to condition operator('==')
