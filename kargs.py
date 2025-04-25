# def print_backwards(*args, file=None):
# def print_backwards(*args, end='',**kwargs):
# def print_backwards(*args, **kwargs):
#     print(kwargs)
#     kwargs.pop('end', None)
#     # keyword = kwargs.pop('end', None)
#     for word in args[::-1]:
#         # print(word[::-1], end=' ', file=file)
#         print(word[::-1], end=' ', **kwargs)
#         # print(word[::-1], end=keyword, **kwargs)


def print_backwards(*args,  **kwargs):
    # print(kwargs)
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    # for word in args[::-1]:
    for word in args[:0:-1]: # change the range
        # print(word[::-1], end=' ', file=file)
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)  # and print the first word separately
    # print(end=end_character) # which means we don't need this line


def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader",  end='\n')
    print("Another String")

print()
# print("hello", "planet", "earth", "take", "me", "to", "your", "leader",  end='\n', sep='|')
print("hello", "planet", "earth", "take", "me", "to", "your", "leader",  end='', sep='\n**\n')
# print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader",  end='\n', sep='|')
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader",  end=' ', sep='\n**\n')
backwards_print("hello", "planet", "earth", "take", "me", "to", "your", "leader",  end=' ', sep='\n**\n')

print("="*10)
