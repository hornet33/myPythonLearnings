# Python program to simulate a quiz game
from data import *
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []  # Empty list to store the Question objects for each question/answer pair

# for item in question_data:
for item in new_data:  # Loop through all questions in the new_data list
    q = Question(item["question"], item["correct_answer"])  # Create a new object which has the question and answer
    question_bank.append(q)  # Append the question object to the question_bank list

quiz_brain = QuizBrain(question_bank)  # Create a QuizBrain object with the question_bank list

while quiz_brain.still_has_questions():  # Iterate while there are still questions left in the list
    quiz_brain.next_question()  # Ask the next question to the user and maintain the score based on response

# Final statement to show quiz complete and final score of the user
print(f"You have completed the quiz. Your final score: {quiz_brain.score} / {len(question_bank)}")
