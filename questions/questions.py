from random import randint


class Questions:
    def __init__(self, questions):
        self.questions = questions

    def get_question(self):
        return self.questions.pop(randint(0, len(self.questions) - 1))
