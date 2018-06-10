import unittest
from pack import Pack
from album import Album

class TestAlbum(unittest.TestCase):

    def test_pack_size(self):
        pack = Pack()

        stickers = pack.open()
        pack_size = len(stickers)

        self.assertEqual(pack_size, 5)


    def test_album_size(self):
        album = Album()

        album_size = len(album.structure)

        self.assertEqual(album_size, 682)


    def test_album_initially_void(self):
        album = Album()

        stickers_album = album.get_sticker()

        self.assertEqual(stickers_album, [])


    def test_insert_sticker(self):
        album = Album()
        stickers = [1, 2, 4, 5, 6]

        album.insert_sticker(stickers)
        stickers_album = album.get_sticker()

        self.assertEqual(stickers_album, [1, 2, 4, 5, 6])


    def test_get_repeated_sticker(self):
        album = Album()
        stickers = [1, 3, 3, 4, 5, 6, 1, 10, 11, 11, 15, 3]

        album.insert_sticker(stickers)
        repeated_stickers = album.get_repeated_sticker()

        self.assertEqual(repeated_stickers, {1: 1, 3: 2, 11: 1})
        # self.assertEqual(repeated_stickers, [1, 3, 11)
        #perguntar sobre esse caso, o teste inicialmente era mais simples e quando fiz o póximo
        #esse deixou de passar, e com as alteracoes ele passou a ser exatamente o teste embaixo
        #deixei os dois apenas para questionamento

    def test_get_number_of_repeated_sticker(self):
        album = Album()
        stickers = [1, 1, 1, 1, 3, 3, 4, 5, 6, 10, 10, 11, 11, 15, 15, 15, 15]

        album.insert_sticker(stickers)
        repeated_stickers = album.get_repeated_sticker()

        self.assertEqual(repeated_stickers, {1: 3, 3: 1, 10: 1, 11: 1, 15: 3})


    def test_get_missing_sticker(self):
        album = Album()
        stickers = [sticker for sticker in range(1, 651)]

        album.insert_sticker(stickers)
        missing_stickers = album.get_missing_sticker()

        self.assertEqual(missing_stickers, [sticker for sticker in range(651, 683)])


    def test_get_report(self):
        album = Album()
        stickers = [sticker for sticker in range(1, 651)]
        stickers_ = [1, 5, 5, 9, 10, 11, 50, 345]
        #the second list is to generate some diferential and repeated stickers

        album.insert_sticker(stickers)
        album.insert_sticker(stickers_)
        album_report = album.get_report()

        self.assertEqual(album_report, {'missing':32, 'repeated':8, 'obtained':650})


if __name__ == '__main__':
    unittest.main()
