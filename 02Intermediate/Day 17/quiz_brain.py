class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        q_object = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}: {q_object.question} (True/False): ").lower()
        self.check_answer(user_answer, q_object.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_ans, correct_ans):
        if user_ans == correct_ans.lower():
            print("That's the right answer.")
            self.score += 1
        else:
            print(f"That's not the right answer - the right answer is {correct_ans}")
        print(f"Your current score is {self.score}")
        print("")
