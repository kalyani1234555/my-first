from nested_data import albums
# print(albums)
SONGS_LIST = 3
SONGS_INDEX_LIST = 1
songs_list = 0
while True:
    print("Please choose your album (invalid choice exists):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index +1, title))
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST]
    else:
          break
    print("Please choose your songs:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index+1, song))
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONGS_INDEX_LIST]
        print("playing {}".format(title))
    # else:
    #     break
    # print(songs_list[song_choice - 1])

    print("=" * 40)
    # print(albums[choice - 1])
    # print(songs_list)
    # print()
    # for index, (title, artist, year, songs) in enumerate(albums):
    #     print("{}: {}, {}, {}, {}".format(index +1, title, artist, year, songs))
    # for index, value in enumerate(albums):
    #     print(index, value)
    # for index, value in enumerate(albums):
    #     title, artist, year, songs = value
    #     print(index, title, artist, year, songs)
    # break
