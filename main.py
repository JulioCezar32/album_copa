from album import Album
from pack import Pack
opened_number = []
for number_of_test in range (10):
    album = Album()
    pack = Pack()
    opened_packs = 0
    album_report = album.get_report()
    missing = album_report['missing']
    while missing > 50:

        album.insert_sticker(pack.open())
        album_report = album.get_report()
        missing = album_report['missing']
        opened_packs += 1

    report = album.get_report()

    opened_number.append(opened_packs)
    print('album processed {}'.format(number_of_test + 1))

print('min number of packs {}'.format(min(opened_number)))
print('max number of packs {}'.format(max(opened_number)))
print('mean of packs {}'.format(sum(opened_number)/10))
