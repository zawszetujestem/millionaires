from player import Player
from questions import Question


class Game:
    def __init__(self, player, questions, gui):
        self.name = player
        self.gui = gui
        self.questions = questions
        self.question = self.questions.get_question()
        self.guaranteed_levels = [2, 5, 8]
        self.money_level = [500, 1000, 5000, 10000, 25000, 50000, 100000, 250000, 500000, 1000000]
        self.question_no = 1
        self.lifelines = ['Fifty Fifty', 'Call to friend', 'Audience ask']
        self.lifelines_done = []

    def play(self):
        self.gui.welcome(self.name)

        while True:

            self.gui.show_dashboard(self.question_no, self.guaranteed_levels, self.money_level)

            self.gui.show_question(self.question.question, self.question.answers)
            option = self.gui.player_options()

            if option == "1":
                user_answer = self.gui.get_player_answer()
                if user_answer.upper() == self.question.get_answer_letter():
                    print("This is correct answer")
                    self.question_no += 1
                    self.question = self.questions.get_question()
                else:
                    print(f"This answer is wrong.")
                    self.end_game()
                    return
            elif option == "2":
                user_lifeline = self.gui.get_user_lifeline(self.lifelines, self.lifelines_done)
                if user_lifeline == "1" and "Fifty Fifty" not in self.lifelines_done:
                    self.question.fifty_fifty_wheel()
                    self.lifelines_done.append("Fifty Fifty")
                elif user_lifeline == "2" and "Call to friend" not in self.lifelines_done:
                    print(self.question.call_to_friend())
                    self.lifelines_done.append("Call to friend")
                elif user_lifeline == "3" and "Audience ask" not in self.lifelines_done:
                    print(self.question.audience_ask())
                    self.lifelines_done.append("Audience ask")
                else:
                    print(f"There is no option {user_lifeline}")
            else:
                self.user_end_game()
                return
                # print(f"You win {self.money_level[self.question_no - 1]}. Congrats!")

    def user_end_game(self):
        if self.gui.play_again().upper() == 'Y':
            self.question_no = 1
            self.play()
        else:
            self.gui.show_result(self.money_level[self.question_no - 2])
            return

    def end_game(self):
        if self.gui.play_again().upper() == 'Y':
            self.question_no = 1
            self.play()
        else:
            self.gui.show_result(self.total_score())
            return

    def total_score(self):
        for idx, level in enumerate(self.guaranteed_levels):
            if level >= self.question_no:
                if idx == 0:
                    return 0
                return self.money_level[self.guaranteed_levels[idx - 1] - 1]
