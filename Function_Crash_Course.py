


def make_album(artist_name, album_title, num_songs=None):
    dictionary = {
        "name": artist_name,
        "title": album_title
    }
    if num_songs:
        dictionary["total songs"] = num_songs
    return dictionary

print("(Press 'q' to quit) ")
while True:
    name_artist = input("Enter the name of artist: ")
    if name_artist.lower() == "q":
        break
    name_album = input("Enter the name of album: ")
    if name_album == "q":
        break
    print(make_album(name_artist, name_album))





