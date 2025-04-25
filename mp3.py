import os
import fnmatch
import id3reader_p3 as id3reader


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)  # create absolute path, use it in yeild values
            # yield os.path.join(path, file)
            yield os.path.join(absolute_path, file)


my_music_files = find_music('music', 'emp3')
# my_music_files = find_music(path, 'mp3') # mp3 file will work because it's not a text file, it's reader, emp3 are text

error_list = []
for f in my_music_files:
    try:
        id3r = id3reader.Reader(f)
        print("Artist: {}, Album: {}, Track: {}, song: {}". format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title'),
        ))
    except:
        error_list.append(f)
    # print(f)


for error_file in error_list:
    print(error_file)

# for f in my_music_files:
#     print(f)
# for f in find_music('music', 'emp3'):
#     print(f)
