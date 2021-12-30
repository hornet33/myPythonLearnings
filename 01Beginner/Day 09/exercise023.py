# Python program to grade students based on scores and save in a new dictionary
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# Create an empty dictionary called student_grades.
student_grades = {}

# Add grades to student_grades
for student in student_scores:  # Loop through each student in the dictionary
    score = student_scores[student]  # Get current student score from student_scores and save in a variable

    # Check score against the grading rules and assign grade accordingly in the student_grades dictionary
    if 91 <= score <= 100:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
