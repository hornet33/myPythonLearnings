# In Python, a dictionary is a {key: value} pair - like maps in Java
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
# Access dictionary elements by the key - key must be exactly the same including case
print(programming_dictionary["Bug"])
print(programming_dictionary.get("Bug"))

# Dictionary is ordered, does not allow duplicate values (last value over-writes the key-value)
my_car_dictionary = {
    "Brand": "Renault",
    "Model": "Duster",
    "Make": "2017",
    "Make": "2021",  # This value will be taken for "Make", not "2017"
}
print(my_car_dictionary)

# Adding elements to a dictionary
my_car_dictionary["Transmission"] = "Automatic"
print(my_car_dictionary)

# Loop through individual dictionary items
for key in my_car_dictionary:
    print(f"{key} = {my_car_dictionary.get(key)}")

# Create an empty dictionary (initialize)
new_dictionary = {}

# Clear a dictionary
my_car_dictionary = {}  # Wipes out the dictionary and sets it to an empty dictionary
print(my_car_dictionary)
