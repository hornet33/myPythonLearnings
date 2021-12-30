# Python program to pick a random name to pay the bill from a list of names

import random

names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(",")  # Split string method - similar to Java split method
total_names = len(names)  # Get the length of the names list
person_who_will_pay = names[random.randint(0, total_names - 1)]  # Randomly generate an int from 0 to total names - 1
print(person_who_will_pay + " is going to buy the meal today!")  # Print the output

# There is a built-in method random.choice() which will give the same result without using randint()
print(random.choice(names) + " is going to buy the meal today!")
