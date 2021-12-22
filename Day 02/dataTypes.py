# Strings and subscripts
s = "Hello"  # This is a string
c = s[0]  # Will assign 'H' to variable 'c' - this is called a subscript in Python

print(s + " " + c)

# Integers
i = 123
print(i)
i = 123_123_123  # In Python we can give underscore to separate number places like thousands, millions, etc for better readability
print(i)

# Floats - numbers with decimals
f = 123.34
print(f)
f = 123_123_349.25
print(f)

# Booleans - True or False (case-sensitive - cannot be 'true' or 'TRUE', must be only 'True' or 'False')
b = True
print(b)
# b = false -- this statement will give an error
b = False
print(b)

# # # type function to check the type of data
print(type(s))
print(type(i))
print(type(f))
print(type(b))

# # # type conversion / type casting - converting from one data type to another
# print("Value of i = " + i)
# The above line will give an error since print takes only a single datatype; here i is of type int and rest is type str
print("Value of i = " + str(i))  # This will convert int i to type str and print will accept it
print(70 + float("100.5"))
print(str(70) + str(100.5))
