# Syntax: new_dictionary = {new_key:new_value for item in list if test}
import random

names = ["Anil", "Binod", "Chanakya", "Dev", "Eshwar", "Feroz"]
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score >= 40}
print(passed_students)
