from random import choices, randint


class Question:
    def __init__(self, question, answers, correct_id):
        self.correct_id = correct_id - 1
        self.question = question
        self.answers = answers
        self.answers_letter = ['A', 'B', 'C', 'D']

    def get_correct_answer(self):
        return self.answers[self.correct_id]

    def get_answer_letter(self):
        return self.answers_letter[self.correct_id]

    def fifty_fifty_wheel(self):
        uncorrected_answers = [answer for idx, answer in enumerate(self.answers) if idx != self.correct_id]
        del_two_answers = choices(uncorrected_answers, k=1)
        self.answers = [answer if idx == self.correct_id or answer == del_two_answers[0] else "" for idx, answer in
                        enumerate(self.answers)]

    def call_to_friend(self):
        know = randint(0, 1)
        half = len([answer for answer in self.answers if answer]) == 2
        if know or half:
            new_answers = [answer for idx, answer in enumerate(self.answers) if idx != self.correct_id]
            incorrect_answers = choices(new_answers, k=1)
            return choices([incorrect_answers[0], self.answers[self.correct_id]], k=1)[
                       0], "I think this is correct answer"
        else:
            return choices(self.answers, k=1), "I am not pretty sure that is correct answer"

    def audience_ask(self):
        answers = self.answers_letter
        correct_answer = self.answers_letter[self.correct_id]
        total = 100
        prob_ca = randint(30, 90)
        total -= prob_ca

        for idx, letter in enumerate(self.answers_letter):
            if letter == correct_answer:
                answers[idx] = f"{letter}: {prob_ca}%"
            else:
                prob = randint(0, total)
                total -= prob
                answers[idx] = f"{letter}: {prob}%"

        return answers
