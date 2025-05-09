import sqlite3
try:
    import tkinter
except ImportError:  # python 2
    import TKinter as tkinter

# conn = sqlite3.connect('music.sqlite')


class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        # tkinter.Listbox.__init__(self, window, **kwargs) #python 2
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        # tkinter.Listbox.grid(self, row=row, column=column, sticky=sticky, rowspan=rowspan, **kwargs) #python 2
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        # Scrollbox.__init__(self, window, **kwargs) # python 2
        super().__init__(window, **kwargs)

        self.cursor = connection.cursor()
        self.table = table
        self.field = field
        self.linked_box = None
        self.linked_field = None

        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = "SELECT " + self.field + ", _id" + "FROM" + self.table
        if sort_order:
            self.sql_sort = "ORDER BY " + ','.join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        if link_value and self.link_field:
            sql = self.sql_select + "WHERE" + "self.linked_field" + "=?" + self.sql_sort
            print(sql)  # TODO delete this line
            self.cursor.execute(sql, (link_value,))
        else:
            print(self.sql_select + self.sql_sort)  # TODO delete this title
            self.cursor.execute(self.sql_select + self.sql_sort)

        # clear the listbox contents before re-loading
        self.clear()

        if self.linked_box:
            self.linked_box.clear()

        for value in self.cursor:
            self.insert(tkinter.END, value[0])

    def on_select(self, event):
        if self.linked_box:
            print(self is event.widget)  # TODO delete this line
            index = self.curselection()[0]
            value = self.get(index)
            # get the artist ID from the database row
            link_id = self.cursor.execute(self.sql_select + "WHERE" + self.field + "=?", value).fetchone()[1]
            # albumList.requery(link_id)
            self.linked_box.requery(link_id)


if __name__ == '__main__':
    conn = sqlite3.connect('music.sqlite')


    mainWindow = tkinter.Tk()
    mainWindow.title('Music DB Browser')
    mainWindow.geometry('1024x768')

    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=2)  # spacer column on right

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=5)
    mainWindow.rowconfigure(2, weight=5)
    mainWindow.rowconfigure(3, weight=1)

    # -----------labels----------
    tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
    tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
    tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

    # --------Artists Listbox----
    # artistList = tkinter.Listbox(mainWindow)
    # albumList = Scrollbox(mainWindow, listvariable=albumLV)
    artistList = DataListBox(mainWindow, conn, "artists", "name")
    artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
    artistList.config(border=2, relief='sunken')

    # artistScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistList.yview)
    # artistScroll.grid(row=1, column=0, sticky='nse', rowspan=2)
    # artistList['yscrollcommand'] = artistScroll.set

    # for artistList in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
    #     artistList.insert(tkinter.END, artist[0])

    # artistList.requery(12)

    # artistList.bind('<<ListboxSelect>>', get_albums)

    # ---------Albums Listbox -----
    albumLV = tkinter.Variable(mainWindow)
    albumLV.set(("choose an artist",))
    # albumList = tkinter.Listbox(mainWindow, listvariable=albumLV)
    # albumList = Scrollbox(mainWindow, listvariable=albumLV)
    albumList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",))
    albumList.requery()
    albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
    albumList.config(border=2, relief='sunken')

    # albumList.bind('<<ListboxSelect>>', get_songs)
    artistList.link(albumList, "artist")

    # albumScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=albumList.yview)
    # albumScroll.grid(row=1, column=1, sticky='nse', rowspan=2)
    # albumList['yscrollcommand'] = albumScroll.set

    # -----------Songs Listbox------
    songLV = tkinter.Variable(mainWindow)
    songLV.set(("choose an album",))
    # songList = tkinter.Listbox(mainWindow, listvariable=songLV)
    # songList = Scrollbox(mainWindow, listvariable=songLV)
    songList = DataListBox(mainWindow, conn, "songs", "title", ("track", "title"))
    # songList.requery()
    songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
    songList.config(border=2, relief='sunken')

    albumList.link(songList, "album")

    # -----------main loop------
    # testlist = range(1, 100)
    # albumLV.set(tuple(testlist))
    # albumLV.set((1, 2, 3, 4, 5))
    mainWindow.mainloop()
    print("closing database connection")
    conn.close()
