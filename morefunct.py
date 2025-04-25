import math
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


# def parabola(x):
#     # y = x * x
#     y = x * x / 100
#     return y

def parabola(page, size):
    # for x in range(-size, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)
        # print(x)
        # print(y)


# Modify circle function so that it  allows the color of the circle to be specified
# and defaults to red if a color is not given. You may want to review the previous lectures
# about named parameters and default values.


def circle(page, radius, g, h, colour="red"):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour, width=2)
    # for x in range(g, g + radius):
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     print(x)
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page):
    page.update()
    # x_origin = canvas.winfo_width()/2
    # y_origin = canvas.winfo_height()/2
    x_origin = page.winfo_width()/2
    y_origin = page.winfo_height()/2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill='black')
    page.create_line(0, y_origin, 0, -y_origin, fill='black')
    print(locals())

def plot(page, x, y):
    canvas.create_line(x, -y, x+1, -y+1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

# canvas = tkinter.Canvas(mainWindow, width=320, height=480)
# canvas.grid(row=0, column=0)

# canvas1 = tkinter.Canvas(mainWindow, width=320, height=480, background='blue')
# canvas1.grid(row=0, column=1)

# print(repr(canvas), repr(canvas1))
draw_axes(canvas)
# draw_axes(canvas1)

# for x in range(-100, 100):
#     y = parabola(x)
    # print(y)
    # print(x)
    # plot(canvas, x, -y)

parabola(canvas, 100)
parabola(canvas, 200)

circle(canvas, 100, 100, 100, "blue")
circle(canvas, 100, 100, -100, "black")
circle(canvas, 100, -100, 100, "green")
circle(canvas, 100, -100, -100, "yellow")
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)


mainWindow.mainloop()
