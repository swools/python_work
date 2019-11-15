def make_album(artist, album, songs=None):
    new_album = {'artist': artist, 'album': album}
    if songs:
        new_album['songs'] = songs
    return new_album

album = make_album('Taking Back Sunday', 'Louder Now') 
print(album)
album = make_album('Post Malone', 'Hollywood is Bleeding')
print(album)
album = make_album('Lil Wayne', 'Tha Carter III', songs=18) 
print(album)