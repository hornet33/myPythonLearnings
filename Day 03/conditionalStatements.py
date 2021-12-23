# Python conditional operators and control flow with if / else statements
# Indentation and spacing is crucial in Python - no braces like Java, an if/else block is recognized by the indentation
i = int(input("Enter your height in cm: "))
bill = 0
if i >= 120:
    a = int(input("Enter your age in years: "))
    
    # # # Nested Conditions
    if a >= 18:
        bill = 12
        print("One adult ticket is $12")
    elif a >= 12:  # Else if
        bill = 7
        print("One youth ticket is $7")
    else:
        bill = 5
        print("One child ticket is $5")

    # # # Multiple if blocks
    want_photo = input("Do you want a photo of the ride? Y or N: ")
    if want_photo.upper() == "Y":
        bill += 3
        print("One ride photo is $3")

    print(f"Your total bill is ${bill}")
else:
    print("Sorry, you cannot ride the roller-coaster!")

# Logical operators
