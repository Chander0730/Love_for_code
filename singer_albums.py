def make_album(singer_name, album_name, number=''):
    albums = {'singer': singer_name, 'album': 'album_name'}
    if number:
        albums['number'] = number
    return albums

while True:
    print("\nPlease tell me a singer'name and album'name")
    print("(enter 'q' to quit )")
    singer_name = input("Please enter singer name: ")
    if singer_name == 'q':
        break
    album_name = input("Please enter album name: ")
    if album_name == 'q':
        break
    print(make_album(singer_name, album_name))
