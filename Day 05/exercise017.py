# Python program to find the highest score in a class

# Take the input and store as an integer list
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# Finding the max score in the list
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}")
