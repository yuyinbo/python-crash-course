def make_album(singer, album, number=None):
    singer_info = {'singer_name': singer, 'album_name': album}
    # if number:
    #     singer_info['song_number'] = number
    if number is not None:
        singer_info['song_number'] = number
    return singer_info


while True:
    print("enter 'q' at any time to quit")
    singer = input("Who's the singer? ")
    if singer == 'q':
        break
    album = input("What's the name of the album? ")
    if album == 'q':
        break
    number = input("How many songs in the album?(optional) ")
    if number == 'q':
        break
    elif number != '':
        number = int(number)
    else:
        number = None
    print(make_album(singer, album, number))
