# Example function with no parameters, no return data
def greet_function():
    print("Line 1")
    print("Line 2")
    print("Line 3")


greet_function()  # Calling the function


# Example function with a simple parameter, no return data
def greet_name(name):
    print(f"Hello {name}, how are you today?")


greet_name("Rahul")


# Example function with more than one parameter, no return data
def greet_with(name, location):
    print(f"Hello {name}, how is the weather today in {location}?")


greet_with("Rahul", "Siliguri")  # These are called 'positional' arguments - function takes args based on the position
greet_with(location="Siliguri", name="Rahul")  # These are 'keyword' arguments - position doesn't matter
