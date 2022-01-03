# Class to run the quiz
class QuizBrain:
    def __init__(self, q_list):  # Constructor to initialize the question list, question num and score
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        """Method to show the next question in the list to the user, get user response and check the answer"""
        q_object = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}: {q_object.question} (True/False): ").lower()
        self.check_answer(user_answer, q_object.answer)

    def still_has_questions(self):
        """Method to return True if the question list has questions remaining, else returns False"""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_ans, correct_ans):
        """Method to compare user answer against the correct answer for the question and updates score"""
        if user_ans == correct_ans.lower():
            print("That's the right answer.")
            self.score += 1
        else:
            print(f"That's not the right answer - the right answer is {correct_ans}")
        print(f"Your current score is {self.score}")
        print("")
