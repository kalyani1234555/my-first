import os

root = "music"

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            # songs_details = f.strip('.emp3').split(' _ ')
            songs_details = f[:-5].split(' - ')
            print(songs_details)
        print('*' * 40)
    # print(path)
    # print(directories)
    # print(files)
    # input()
    # for f in files:
    #     print("\t{}".format(f))
