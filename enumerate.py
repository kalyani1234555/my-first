# for index, character in enumerate("abcdef"):
#     print(index, character)
# list1 = [23, 3, 6, 5, 12, 9, 7, 4]
# min_num = 7
# index = list1.index(min_num)
# print(index)

# for t in enumerate("abcdef"):
#     print(t)

for t in enumerate("abcdef"):
    index, character = t
    print(index, character)

index, character = (0, 'a')
print(index)
print(character)
