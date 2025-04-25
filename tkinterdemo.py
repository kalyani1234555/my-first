# import TKinter as tkinter
try:
    import tkinter
except ImportError:  # python 2
    import TKinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

tkinter._test()

mainwindow = tkinter.Tk()

mainwindow.title("Hello World")
mainwindow.geometry('640x480+8+400')
mainwindow.mainloop()
