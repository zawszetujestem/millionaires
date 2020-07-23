from player import Player


class Game:
    def __init__(self, questions, gui):
        self.gui = gui
        self.questions = questions
        self.guaranteed_levels = [2, 5, 8]
        self.money_level = [500, 1000, 5000, 10000, 25000, 50000, 100000, 250000, 500000, 1000000]
        self.question_no = 1

    def play(self):
        self.name = Player
        self.name = input("Enter your name:\n")

        self.gui.welcome(self.name)

        self.gui.show_dashboard(self.question_no, self.guaranteed_levels, self.money_level)

        # while True:
        #
        #     if True:
        #         print("Next round")
        #     else:
        #         print("You lose")
        #         break
