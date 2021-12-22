# Python conditional operators and control flow with if / else statements
# Indentation and spacing is crucial in Python - no braces like Java, an if/else block is recognized by the indentation
i = int(input("Enter your height in cm: "))
if i >= 120:
    a = int(input("Enter your age in years: "))
    # # # Nested Conditions
    if a >= 18:
        print("The ticket price is $12")
    elif a >= 12:  # Else if
        print("The ticket price is $7")
    else:
        print("The ticket price is $5")
else:
    print("Sorry, you cannot ride the roller-coaster!")
