import os
import fnmatch


def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        caps_name = artist_name.upper()
        # print(directories)
        # for artist in directories:
        # for artist in fnmatch.filter(directories, artist_name):
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):
            subdir = os.path.join(path, artist)
            # print(path)
            # print(artist)
            print(subdir)
            for album_path, albums, _ in os.walk(subdir):
                print(album_path)
                # print(albums)
                for album in albums:
                    # print(albums)
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        print(album)
        for song in os.listdir(album[0]):  # we want the path, not of the album
            yield song
#
#
album_list = find_albums("music", "Aerosmith")
album_list = find_albums("music", "black*")
song_list = find_songs(album_list)

# for a in album_list:
#     print(a)

for s in song_list:
    print(s)
