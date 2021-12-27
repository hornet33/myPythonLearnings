# Python program to print the average height of students

# Take the input and store in a list
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):  # Can also use "range(len(student_heights))" as default start index = 0
    student_heights[n] = int(student_heights[n])

# Variables to store total students and total height of all students
total_students = 0
total_height = 0
for student_height in student_heights:
    total_students += 1  # Add one to total students
    total_height += student_height  # Add to the total height

# Calculate average height rounded to the nearest integer
average_height = round(total_height / total_students)
print(average_height)
