import unittest
from pacote import Pacote
from album import Album

class TestAlbum(unittest.TestCase):

    def test_pacote_size(self):
        pacote = Pacote()

        figurinhas = pacote.open()
        pacote_size = len(figurinhas)

        self.assertEqual(pacote_size, 5)


    def test_album_size(self):
        album = Album()

        album_size = len(album.structure)

        self.assertEqual(album_size, 682)

    def test_album_

if __name__ == '__main__':
    unittest.main()
