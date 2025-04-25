try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

import os
mainwindow = tkinter.Tk()

mainwindow.title("Grid Demo")
mainwindow.geometry('640x480-8-200')
mainwindow['padx'] = 8

label = tkinter.Label(mainwindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

mainwindow.columnconfigure(0, weight=100)
mainwindow.columnconfigure(1, weight=1)
mainwindow.columnconfigure(2, weight=1000)
mainwindow.columnconfigure(3, weight=600)
mainwindow.columnconfigure(4, weight=1000)
mainwindow.rowconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=10)
mainwindow.rowconfigure(2, weight=1)
mainwindow.rowconfigure(3, weight=3)
mainwindow.rowconfigure(4, weight=3)

filelist = tkinter.Listbox(mainwindow)
filelist.grid(row=1, column=0, sticky='nsew', rowspan=2)
filelist.configure(border=2, relief='sunken')
for zone in os.listdir('/Windows/System32'):  #/usr/bin
    filelist.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainwindow, orient=tkinter.VERTICAL, command=filelist.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
filelist['yscrollcommand'] = listScroll.set

# frame for the radio buttons
optionFrame = tkinter.LabelFrame(mainwindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='ne')

rbvalue = tkinter.IntVar()
rbvalue.set(3)

# radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbvalue)
radio2 = tkinter.Radiobutton(optionFrame, text="path", value=2, variable=rbvalue)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbvalue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# widget to display the result
resultlabel = tkinter.Label(mainwindow, text="Result")
resultlabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainwindow)
result.grid(row=2, column=2, sticky='ew')
# result.grid(row=2, column=2, sticky='sw')

# frame for the time spinners
timeframe = tkinter.LabelFrame(mainwindow, text="Time")
timeframe.grid(row=3, column=0, sticky='new')
# Time spinners
hoursspinner = tkinter.Spinbox(timeframe, width=2, values=tuple(range(0, 24)))
minutesspinner = tkinter.Spinbox(timeframe, width=2, from_=0, to=59)
secondsspinner = tkinter.Spinbox(timeframe, width=2, from_=0, to=59)
hoursspinner.grid(row=0, column=0)
tkinter.Label(timeframe, text=":").grid(row=0, column=1)
minutesspinner.grid(row=0, column=2)
tkinter.Label(timeframe, text=":").grid(row=0, column=3)
secondsspinner.grid(row=0, column=4)
timeframe['padx'] = 36

# frame for the date spinners
dateframe = tkinter.Frame(mainwindow)
dateframe.grid(row=4, column=0, sticky='new')
# date labels
daylabel = tkinter.Label(dateframe, text = "Day")
monthlabel = tkinter.Label(dateframe, text = "Month")
yearlabel = tkinter.Label(dateframe, text = "Year")
daylabel.grid(row=0, column=0, sticky='w')
monthlabel.grid(row=0, column=1, sticky='w')
yearlabel.grid(row=0, column=2, sticky='w')
#date spinners
dayspin = tkinter.Spinbox(dateframe, width=5, from_=1, to=31)
monthspin = tkinter.Spinbox(dateframe, width=5, value = ("Jan","Feb","Mar","Mar","Apr","May","Jun","July","Aug","Sep","Nov","Dec"))
yearspin = tkinter.Spinbox(dateframe, width=5, from_=2000, to=2099)
dayspin.grid(row=1, column=0)
monthspin.grid(row=1, column=1)
yearspin.grid(row=1, column=2)

#buttons
okbutton = tkinter.Button(mainwindow, text="OK")
cancelbutton = tkinter.Button(mainwindow, text="Cancel", command = mainwindow.quit)
# cancelbutton = tkinter.Button(mainwindow, text="Cancel", command = mainwindow.destroy)

okbutton.grid(row=4, column=3, sticky="e")
cancelbutton.grid(row=4, column=4, sticky="w")

mainwindow.mainloop()


print(rbvalue.get())
