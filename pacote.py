import random

class Pacote():
    def __init__(self):
        self._possiveis_figurinhas = range(1, 683)
        self.SIZE = 5

    def open(self):
        self._figurinhas = random.sample(self._possiveis_figurinhas, self.SIZE)
        return self._figurinhas
