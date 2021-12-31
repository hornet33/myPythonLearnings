# Scope of variables in Python

# --- Global variables
enemies = 1


def increase_enemies():
    enemies = 2  # This will create a local instance of a variable with the same name - will give a warning
    print(f"enemies inside function: {enemies}")


def increase_global_enemies():
    global enemies
    enemies = 5  # Using the 'global' keyword before a variable name inside a function to use the global var


increase_enemies()
increase_global_enemies()
print(f"enemies outside function: {enemies}")  # This will invoke the global instance of the 'enemies' variable


# --- Variables inside a function are local, cannot be accessed outside the function
def my_func():
    local_func_var = 2
    print(local_func_var)

# Outside func()
# print(local_func_var)  # Will give a NameError


# --- There is no concept of block scope in Python like other languages
if enemies == 5:  # Refers to global enemies at the top
    my_enemy = "Skeleton"  # New variable inside if block

print(my_enemy)  # Can still access my_enemy outside if block since the variable becomes a global variable

# --- Global Constants are defined in all uppercase
PI = 3.14159

