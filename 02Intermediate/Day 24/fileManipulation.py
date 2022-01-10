# Reading, writing and manipulating files in Python
file = open("my_file.txt")  # Default file opening mode is ready-only
file_contents = file.read()
print(file_contents)
file.close()

file_contents = ""
print(file_contents)

# Cleaner Python way is using "with"
with open("my_file.txt") as file:  # Open in read-only mode
    file_contents = file.read()
    print(file_contents)
    # No need to close the file - Python will do it automatically

# Writing to a file (delete existing content)
with open("my_file.txt", "w") as file:
    file.write("My updated text in file")

with open("my_file.txt") as file:
    file_contents = file.read()
    print(file_contents)

# Appending to a file (keep existing content - add new lines at the end of the file)
with open("my_file.txt", "a") as file:
    file.write("\nAnother line at the end of the file")

with open("my_file.txt") as file:
    file_contents = file.read()
    print(file_contents)

# Create a new file and write contents - will create a file if the file doesn't exist in the current directory
with open("new_file.txt", mode="w") as file:
    file.write("Hello New File!")

# Relative file path - "." is for current, ".." is for one directory up
# "./my_file.txt"
# "../<xyz filename>"
