class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        self.lifeline = []

    @property
    def score(self):
        return f"{self._score} PLN"

    @score.setter
    def score(self, new_score):
        if new_score >= 0:
            self._score = new_score
        else:
            print(f"Score {new_score} is invalid")