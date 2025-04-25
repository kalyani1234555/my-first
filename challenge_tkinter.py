# write a GUI program to create a simple calculator
# layout that looks like a screenshot

# try to be as pythonic as possible - it's ok if you
# end up writing repeated button and grid statements,
# but consider using lists and a for loop
#
# there is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: you may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widget by calling its.update()
# method first.
#
# if you are using windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)],
        ]

mainwindowPadding = 8

mainwindow = tkinter.Tk()
mainwindow.title("Calculator")
mainwindow.geometry('640x480-8-200')
mainwindow['padx'] = mainwindowPadding

result = tkinter.Entry(mainwindow)
result.grid(row=0, column=0, sticky='nsew')

keypad = tkinter.Frame(mainwindow)
keypad.grid(row=1, column=0, sticky='nsew')

row = 0
for keyrow in keys:
    col = 0
    for key in keyrow:
        tkinter.Button(keypad, text=key[0]).grid(row = row, column = col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

mainwindow.update()
# mainwindow.minsize(keypad.winfo_width() + mainwindowPadding, result.winfo_height() + keypad.winfo_height())
# mainwindow.maxsize(keypad.winfo_width() +50 + mainwindowPadding, result.winfo_height() + 50 + keypad.winfo_height())
mainwindow.maxsize(keypad.winfo_width() + mainwindowPadding , result.winfo_height() + keypad.winfo_height())

mainwindow.mainloop()
