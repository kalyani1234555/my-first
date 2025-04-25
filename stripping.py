def removeprefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix)]
    else:
        return string[:]  #Return a copy of 'string'


def removesuffix(string: str, suffix: str) -> str:
    if string.endswith(suffix):    # suffix = ' should not call string[:-0]
        return string[-len(suffix)]
    else:
        return string[:]  # Return a copy of 'string'


filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()   # remove \n
print(first)
#
# chars = "'"
# chars1 = "'Twas"
chars2 = "' Twasebv"
# no_apostrophe = first.strip(chars)
# no_apostrophe1 = first.strip(chars1)
# no_apostrophe2 = first.strip(chars2)
# print(no_apostrophe)
# print(no_apostrophe1)
# print(no_apostrophe2)

for character in first:
    if character in chars2:
        print(f'removing"{character}"')
    else:
        break

print('*' * 80)

for character in first[::-1]:
    if character in chars2:
        print(f'removing"{character}"')
    else:
        break

print('*' * 80)

# twas_removed = first.removeprefix("'Twas")
# print(twas_removed)
# toves_removed = first.removesuffix("toves")
# print(toves_removed)


twas_removed = removeprefix(first, "'Twas")
print(twas_removed)
toves_removed = removesuffix(first, "toves")
print(toves_removed)
