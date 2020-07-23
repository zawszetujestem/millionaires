from random import choices


class Question:
    def __init__(self, question, answers, correct_id):
        self.correct_id = correct_id - 1
        self.question = question
        self.answers = answers

    def get_correct_answer(self):
        return self.answers[self.correct_id]

    def fifty_fifty_wheel(self):
        uncorrected_answers = [answer for idx, answer in enumerate(self.answers) if idx != self.correct_id]
        del_two_answers = choices(uncorrected_answers, k=1)
        self.answers = [answer if idx == self.correct_id or answer == del_two_answers[0] else "" for idx, answer in enumerate(self.answers)]
