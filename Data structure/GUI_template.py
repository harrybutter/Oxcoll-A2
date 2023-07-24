# Template for the skeleton of a GUI

# Assuming Python 3
from tkinter import *
# from tkinter import Tk,Menu,Canvas , Message  - did not work
from tkinter.messagebox import showinfo


# see here for discussion on importing classes.
# https://stackoverflow.com/questions/4142151/how-to-import-the-class-within-the-same-directory-or-sub-directory


class ControlBlock:  # Global variables
    def __init__(self):
        # display attributes
        self.canvas = 0
        self.fontSize = 14
        self.title = "GUI Template"
        # version number
        self.verStr = "1.0"
        # author
        self.author = "Fred Smith"
        self.date = "Aug 2022"
        # licence information
        self.licenceStr = \
            "GNU General Public License\n\n" \
            + "This program is free software; you can redistribute it and/or modify it under the terms of the " \
            + "GNU General Public License as published by the Free Software Foundation; " \
            + "either version 2 of the License, or (at your option) any later version.\n\n" \
            + "This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; " \
            + "without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  " \
            + "See the GNU General Public License for more details.\n\n" \
            + "You should have received a copy of the GNU General Public License along with this program; if not, " \
            + "write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA."


# END CLASS

global cb  # controlBlock


def popupShowinfo():
    global cb
    showinfo("About " + cb.title, "Version: " + cb.verStr
             + " " + cb.date + "\n\nAuthor: "
             + cb.author + "\n\n"
             + cb.licenceStr)


def do_exit(root):
    print("performing exit")
    root.destroy()


def main():
    global cb
    cb = ControlBlock()
    # root configuration
    root = Tk()
    root.title(cb.title)
    # https://stackoverflow.com/questions/30965033/python-tkinter-application-fit-on-screen
    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry('%dx%d+0+0' % (width, height))
    root.resizable(True, True)

    # Frame
    # frame = Frame(root, bd=2, relief=SUNKEN)
    frame = Frame(root)

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # menus
    menubar = Menu(root)
    # File
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
    # About
    menubar.add_command(label="About", command=popupShowinfo)

    root.config(menu=menubar)

    # create a canvas for drawing on (if you need it)
    visibleWidth = 1200
    visibleHeight = 700  # a canvas of visible size vW x vH
    cb.canvas = Canvas(frame, bd=0, width=visibleWidth, height=visibleHeight, )
    cb.canvas.grid(row=0, column=0, sticky=N + S + E + W)

    # add a button to implement an action
    # https: //www.geeksforgeeks.org/how-do-you-create-a-button-on-a-tkinter-canvas/
    btnExit = Button(root, text='Exit', width=15, height=2, bd='5', command=lambda: do_exit(root),
                     font=('Arial', cb.fontSize))
    btnExit.place(x=150, y=300)

    frame.pack()
    # place any other initialisation here

    root.mainloop()


# end main()

if __name__ == "__main__":
    main()
