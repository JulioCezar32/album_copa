class Album():

    def __init__(self):
        ALBUM_SIZE = 682

        ALBUM_RANGE = range(1, ALBUM_SIZE + 1)
        self.structure = {empty_space : 0 for empty_space in ALBUM_RANGE}

    def get_sticker(self):
        obtained_stickers = []

        for sticker_position in self.structure:
            if self.structure[sticker_position] >= 1:
                obtained_stickers.append(sticker_position)

        return obtained_stickers

    def insert_sticker(self, new_stickers):
         for sticker_position in new_stickers:
             self.structure[sticker_position] += 1

    def get_repeated_sticker(self):
        repeated_stickers = {}

        for sticker_position in self.structure:
            if self.structure[sticker_position] > 1:
                repeated_number = self.structure[sticker_position] - 1

                repeated_stickers.update({sticker_position:repeated_number})

        return repeated_stickers

    def get_missing_sticker(self):
        missing_stickers = []

        for sticker_position in self.structure:
            if self.structure[sticker_position] == 0:
                missing_stickers.append(sticker_position)

        return missing_stickers

    def get_report(self):
        missing = self.get_missing_sticker()
        obtained = self.get_sticker()
        repeated = self.get_repeated_sticker()

        missing_number = len(missing)
        obtained_number = len(obtained)
        repeated_number = 0
        for repeated_sticker_position in repeated:
            repeated_number += repeated[repeated_sticker_position]

        report = {
            'missing': missing_number,
            'repeated': repeated_number,
            'obtained': obtained_number
            }

        return report
