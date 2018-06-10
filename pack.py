import random

class Pack():
    def __init__(self):
        self._possible_stickers = range(1, 683)
        self.SIZE = 5

    def open(self):
        self._stickers = random.sample(self._possible_stickers, self.SIZE)
        return self._stickers
