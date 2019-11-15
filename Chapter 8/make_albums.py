def make_album(artist, album, songs=None):
    new_album = {'artist': artist, 'album': album}

print("enter 'q' at any time to quit")
while True:
    artist = input("Enter a artist ")
    if artist == 'q':
        break
    album = input("Enter said artist's album name ")
    if album =='q':
        break
    else:
        output = make_album(artist, album)
    print(output)
