from game import Game
from player.player import Player
from questions import Questions
from questions.question import Question
from gui.gui import Gui


q1 = Question("1. What sort of animal is Walt Disney's Dumbo?",
              ['Deer', 'Rabbit', 'Elephant', 'Donkey'],
              3)
q2 = Question("2. What sort of animal is Walt Disney's Dumbo?",
              ['Deer', 'Rabbit', 'Elephant', 'Donkey'],
              3)
q3 = Question("3. What sort of animal is Walt Disney's Dumbo?",
              ['Deer', 'Rabbit', 'Elephant', 'Donkey'],
              3)
q4 = Question("4. What sort of animal is Walt Disney's Dumbo?",
              ['Deer', 'Rabbit', 'Elephant', 'Donkey'],
              3)
q5 = Question("5. What sort of animal is Walt Disney's Dumbo?",
              ['Deer', 'Rabbit', 'Elephant', 'Donkey'],
              3)
q6 = Question("6. What sort of animal is Walt Disney's Dumbo?",
              ['Deer', 'Rabbit', 'Elephant', 'Donkey'],
              3)
q7 = Question("7. What sort of animal is Walt Disney's Dumbo?",
              ['Deer', 'Rabbit', 'Elephant', 'Donkey'],
              3)
q8 = Question("8. What sort of animal is Walt Disney's Dumbo?",
              ['Deer', 'Rabbit', 'Elephant', 'Donkey'],
              3)
q9 = Question("9. What sort of animal is Walt Disney's Dumbo?",
              ['Deer', 'Rabbit', 'Elephant', 'Donkey'],
              3)
q10 = Question("10. What sort of animal is Walt Disney's Dumbo?",
              ['Deer', 'Rabbit', 'Elephant', 'Donkey'],
              3)

questions = Questions([q1, q2, q3, q4, q5, q6, q7, q8, q9, q10])
player = Player("Maniek")
game = Game(player, questions, Gui)

game.play()

