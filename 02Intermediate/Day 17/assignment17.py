from data import *
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
# for item in question_data:
for item in new_data:
    q = Question(item["question"], item["correct_answer"])
    question_bank.append(q)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"You have completed the quiz. Your final score: {quiz_brain.score} / {len(question_bank)}")
