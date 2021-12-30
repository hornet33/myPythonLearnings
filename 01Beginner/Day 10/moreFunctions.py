# Functions which return values - does not need to specify return type like other languages
def some_function():
    return 3 * 2


func_output = some_function()
print(func_output)


# Function to change names to first letter cap and rest lower-case and return the full name
def format_name(f_name, l_name):
    f_name = f_name.title()  # Built-in function title() changes to Title Case (first letter caps, rest lower case)
    l_name = l_name.title()
    return f"{f_name} {l_name}"
    print("This will never get printed since it is after the return statement")

print(format_name("rahul", "pradhan"))


