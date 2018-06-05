class Album():

    def __init__(self):
        ALBUM_SIZE = 682
        self.album_range = range(1, ALBUM_SIZE + 1)
        self.structure = [espaco for espaco in self.album_range]
