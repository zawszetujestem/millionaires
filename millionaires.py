from game import Game
from player.player import Player
from questions import Questions
from questions.question import Question
from gui.gui import Gui


q1 = Question("What sort of animal is Walt Disney's Dumbo?",
              ['Deer', 'Rabbit', 'Elephant', 'Donkey'],
              3)
q2 = Question("In children’s stories, how many wishes are granted by a genie or fairy?",
              ['One', 'Two', 'Three', 'Four'],
              3)
q3 = Question("Which of these is a type of hat?",
              ['Sausage roll', 'Pork pie', 'Scotch egg', 'Potato crisp'],
              2)
q4 = Question("Which of these is not one of the American Triple Crown horse races?",
              [ 'Arlington Million', 'Belmont Stakes', 'Kentucky Derby', 'Preakness Stakes'],
              1)
q5 = Question("Who is the patron saint of Spain?",
              ['St James', 'St John', 'St Benedict', 'St Peter'],
              1)
q6 = Question("The young of which creature is known as a squab?",
              ['Salmon', 'Horse', 'Pigeon', 'Octopus'],
              3)
q7 = Question("In Welsh, what does ‘afon’ mean?",
              ['Fort', 'Meadow', 'Pool', 'River'],
              4)
q8 = Question("Where does a cowboy wear chaps?",
              ['On his head', 'On his arms', 'On his legs', 'On his hands'],
              3)
q9 = Question("Which of these phrases refers to a brief success?",
              ['Blaze in the pot', 'Spark in the tub', 'Flare in the jug', 'Flash in the pan'],
              4)
q10 = Question("Which of these have to pass a test on ‘The Knowledge’ to get a licence?",
              ['Taxi drivers', 'Bus drivers', 'Police officers', 'Ambulance drivers'],
              1)

questions = Questions([q1, q2, q3, q4, q5, q6, q7, q8, q9, q10])
player = Player("Maniek")
game = Game(player, questions, Gui)

game.play()

