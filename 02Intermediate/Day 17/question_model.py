# Class to model the object of each question to be used with two attributes - question and answer
class Question:
    def __init__(self, text, answer):  # Constructor
        self.question = text
        self.answer = answer
