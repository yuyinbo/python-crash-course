def make_album(singer, album, number=None):
    singer_info = {'singer_name': singer, 'album_name': album}
    # if number:
    #     singer_info['song_number'] = number
    if number is not None:
        singer_info['song_number'] = number
    return singer_info


print(make_album("Michael Jackson", "Thriller", 9))
print(make_album("AC/DC", "Back in Black"))
print(make_album("Adele", "21"))
