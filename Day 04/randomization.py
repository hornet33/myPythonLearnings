# Need to import "random" module - similar to importing classes/packages in Java
import random

my_random_int = random.randint(1, 20)  # Picks a random integer between 1 and 20
print(my_random_int)

my_random_float = random.random() * 5
# random.random() picks a random float between 0 and 1 (not inclusive)
# Multiplying with 5 essentially sets the range from 0.00000000 to 4.99999999
print(my_random_float)
print(round(my_random_float, 4))  # Rounding the random float to 4 decimal places
print("{:.4f}".format(my_random_float))  # Formatting to 4 decimal places without round()
