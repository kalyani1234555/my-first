def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    # print("spam and eggs")
    print(" " * left_margin, text)


# def centre_text(text1):
# def centre_text(*args, sep=" ", end='\n', file=None, flush=False):
def centre_text(*args, sep=" "):
    # text1 = str(args)
    text1 = " "
    for arg in args:
        text1 += str(arg) + sep
        # text1 += str(arg) + " "
    left_margin = (80 - len(text1)) // 2
    # print(" " * left_margin, text1, end=end, file=file, flush=flush)
    # return " " * left_margin, text1
    return " " * left_margin + text1


# with open("centred", mode='w') as centred_file:

     # call the function
     # print(python_food())
     # python_food()
     # centre_text("Spam and eggs", file=centred_file)
     # centre_text("Spam, Spam and eggs", file=centred_file)
     # centre_text(12, file=centred_file)
     # centre_text("Spam, Spam, Spam and Spam", file=centred_file)

     # print("first", "second", 3, 4, "spam")
     # centre_text("first", "second", 3, 4, "spam", sep=':', file=centred_file)

# print(centre_text("Spam and eggs"))
# print(centre_text("Spam, Spam and eggs"))
# print(centre_text(12))
# print(centre_text("Spam, Spam, Spam and Spam"))
# print(centre_text("first", "second", 3, 4, "spam", sep=':'))

# centre_text("Spam and eggs")
# centre_text("Spam, Spam and eggs")
# centre_text(12)
# centre_text("Spam, Spam, Spam and Spam")
# centre_text("first", "second", 3, 4, "spam", sep=':')

# print("Spam and eggs")
# print("Spam, Spam and eggs")
# print(12)
# print("Spam, Spam, Spam and Spam")
# print("first", "second", 3, 4, "spam", sep=':')

# s1 = centre_text("Spam and eggs")
# print(s1)
# s2 = centre_text("Spam, Spam and eggs")
# print(s2)
# s3 = centre_text(12)
# print(s3)
# s4 = centre_text("Spam, Spam, Spam and Spam")
# print(s4)
# s5 = centre_text("first", "second", 3, 4, "spam", sep=":")
# print(s5)

with open("Menu", mode="w") as menu:
    s1 = centre_text("Spam and eggs")
    print(s1, file=menu)
    s2 = centre_text("Spam, Spam and eggs")
    print(s2, file=menu)
    print(centre_text(12), file=menu)
    print(centre_text("Spam, Spam, Spam and Spam"), file=menu)
    s5 = centre_text("first", "second", 3, 4, "spam", sep=":")
    print(s5, file=menu)


# print("=" + str(12 * 3))
# print(sorted(['b', 'd', 'c', 'a']))
