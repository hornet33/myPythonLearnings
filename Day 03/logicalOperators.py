# Python uses 'and' , 'or', 'not' as logical operators
# a = 12
# b = 15
# print((a > 14) and (b > 20)) will print False

# The ticketing program from conditionalStatements.py using logical operators
i = int(input("Enter your height in cm: "))
bill = 0
if i >= 120:
    a = int(input("Enter your age in years: "))

    # # # Nested Conditions
    if a >= 45 and a <= 55:
        print("Your ticket is free!")
    elif a >= 18:
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
