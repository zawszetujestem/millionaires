from player.player import Player
from questions.questions import Question

q1 = Question("What sort of animal is Walt Disney's Dumbo?", ['Deer', 'Rabbit', 'Elephant', 'Donkey'], 3)

print(q1.get_correct_answer())
q1.fifty_fifty_wheel()
print(q1.answers)
# player1 = Player("Maniek")
# player1.score = 40
# print(player1.score)
