# t = ("a", "b", "c")
# print(t)
#
# name = "Tim"
# age = 10
#
# print(name,age, "python", 2020)
# print((name,age, "python", 2020))

# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984


# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# metallica2 = list(metallica)
# print(metallica2)
#
# metallica2[0] = "Master of puppets"
# print(metallica2)

# metallica[0] = "Master of puppets"
# print(metallica)

# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
# table = ("coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
#
# name, length, width, height, price = table
# print(length * width)

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
         ("Bad Company", "Bad Company", 1974),
         ("Nightflight", "Budgie", 1981),
         ("More Mayhem", "Emilda May", 2011),
         ("Ride the Lightning", "Metallica", 1984),
         ]
print(len(albums))
for album in albums:
    # print(album)
    # print("Album: {}, Artist: {}, year: {}"
    #       .format(album[0], album[1], album[2]))
    name, Artist, year = album
    print("Album: {}, Artist: {}, year: {}"
          .format(name, Artist, year))

for name, Artist, year in albums:
    print("Album: {}, Artist: {}, year: {}"
          .format(name, Artist, year))
