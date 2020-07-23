from game import Game
from player.player import Player
from questions.questions import Question
from gui.gui import Gui


q1 = Question("What sort of animal is Walt Disney's Dumbo?",
              ['Deer', 'Rabbit', 'Elephant', 'Donkey'],
              3)

game = Game(q1, Gui)

game.play()

# print(q1.get_correct_answer())
# q1.fifty_fifty_wheel()
# print(q1.answers)
# player1.score = 40
# print(player1.score)
