numbers = [1, 2, 3]
new_list = []
for n in numbers:
    new_list.append(n + 1)
print(new_list)

# Using List Comprehension, the above example can be re-written as follows
# Syntax: new_list_name = [new_item for item in original_list]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

# List comprehension also works with strings
name = "Rahul"
new_name = [letter for letter in name]  # Creates a list where each element in the list is a character of the string
print(new_name)

# Also works on ranges
new_range = [n * 2 for n in range(1, 5)]
print(new_range)

# Conditional List Comprehension allows to add a condition to a list comprehension
# Syntax: new_list_name = [new_item for item in original_list if condition]
names = ["Alex", "Beth", "Carol", "David", "Eleanor", "Francis"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)
long_names_caps = [name.upper() for name in names if len(name) >= 5]
print(long_names_caps)
