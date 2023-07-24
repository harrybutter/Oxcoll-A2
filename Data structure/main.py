# Visualisation of an ORDERED linked list
# v1.0 basic drawing functions
#
#
# References
#  Using "is" or "is not" for comparisons with None instead of "==" or "!="
#  PEP 8 states that this should always be done.
#  https://stackoverflow.com/questions/3257919/what-is-the-difference-between-is-none-and-none
#  http://jaredgrubb.blogspot.com/2009/04/python-is-none-vs-none.html

# Assuming Python 3
from tkinter import *
# from tkinter import Tk,Menu,Canvas , Message  - did not work
from tkinter.messagebox import showinfo

from LinkedListSimulator_byNicholas import *


class ControlBlock:    # Global variables
    def __init__(self):
        # store attributes
        self.storeSize = 10
        # display attributes
        self.canvas = 0
        self.operation = "None"
        self.dataEntryValue = "None"
        self.fontSize = 14
        self.dataFill = "orange"  # text colour for data list
        self.freeFill = "green"  # text colour for free list
        # version number
        self.verStr = "1.0"
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


global cb  # controlBlock
global newList  # The linked list object


def popupShowinfo():
    showinfo("About List Visualiser", "Version: " + cb.verStr
             + " March 2022\n\nAuthor: Nicholas Mulvey\n\n"
             + cb.licenceStr)


def drawStore(cb):  # draw the store display
    # constants for graphics dimensions
    bWidth = 200; bHeight = 50  # box dimensions
    x = 300; y = 100  # top left
    freePtrs = newList.getListPtrs("free")
    data, next = newList.getStore()
    print("free list ptrs :", freePtrs)
    print("store ptrs ", next)
    print("store data ", data)

    # draw the store locations
    for box in range(cb.storeSize):
        if box in freePtrs:
            fillCol = cb.freeFill  # free list item
        else:
            fillCol = cb.dataFill  # data list item
        cb.canvas.create_rectangle((x, y, x + bWidth, y + bHeight), width=1, fill=fillCol)
        y = y + bHeight
    # number the store locations
    x = 300; y = 100  # top left
    for i in range(cb.storeSize):
        y = 120 + i * bHeight
        cb.canvas.create_text(x - 20, y, text=str(i), font=('Arial', cb.fontSize), anchor=NW)
        # (NW is top left corner)
    # vertical divider between the data and pointer values
    cb.canvas.create_line((430, 100, 430, 100 + cb.storeSize * bHeight), width=1, fill="black")


def annotateStore():
    data, next = newList.getStore()  # lists of the data and next values for every node
    # print(data)
    x = 350;    y = 120  # top left
    tagStr = "store"
    cb.canvas.delete(tagStr)
    for i in range(cb.storeSize):
        x = 350; y = 120 + i * 50  # bHeight
        cb.canvas.create_text(x, y, text=data[i], tag=tagStr, font=('Arial', cb.fontSize), anchor=NW)
        x = 450
        cb.canvas.create_text(x, y, text=next[i], tag=tagStr, font=('Arial', cb.fontSize), anchor=NW)


def drawPointers(cb, newList):  # display the values of the data and free pointers
    x = 50; y = 100
    dataPtr, freePtr = newList.getPointers()
    label = "data ptr: " + str(dataPtr)
    tagStr = "ptrs"
    cb.canvas.delete(tagStr)
    cb.canvas.create_text(x, y, text=label, tag=tagStr, fill=cb.dataFill,
                          font=('Arial', cb.fontSize), anchor=NW)
    y = y + 50
    label = "free ptr: " + str(freePtr)
    cb.canvas.create_text(x, y, text=label, tag=tagStr, fill=cb.freeFill,
                          font=('Arial', cb.fontSize), anchor=NW)

    cb.canvas.create_text(350, 50, text="Store", font=('Arial', cb.fontSize + 4), anchor=NW)


def drawListDisplay():  # top level routine for drawing each element of the store display
    global cb
    global newList

    drawStore(cb)
    annotateStore()
    drawPointers(cb, newList)

    # display data and free lists
    x = 550; y = 100
    values = newList.getListData("data")
    items = len(values)
    tagStr = "dl1"   # data list element 1 - the label
    cb.canvas.delete(tagStr)
    cb.canvas.create_text(x, y, text="Data List: ("+str(items)+")", tag=tagStr,
                          fill=cb.dataFill, font=('Arial', cb.fontSize), anchor=NW)
    x = 680
    # means of refreshing parts of the display
    # add tag=tagStr to relevant items and then use canvas.delete(tagStr) to delete the tagged items
    # before redrawing them and so displaying the updated value
    tagStr = "dl2"  # data list element 2  - the values
    cb.canvas.delete(tagStr)
    for i in range(items):
        cb.canvas.create_text(x, y, text=str(values[i]), tag=tagStr, font=('Arial', cb.fontSize), anchor=NW)
        x = x + 50

    x = 550; y = 200
    values = newList.getListData("free")
    items = len(values)
    tagStr = "fl1"  # free list element 1 - the label
    cb.canvas.delete(tagStr)
    cb.canvas.create_text(x, y, text="Free List: ("+str(items)+")", tag=tagStr,
                          fill=cb.freeFill, font=('Arial', cb.fontSize), anchor=NW)
    x = 680
    tagStr = "fl2"  # free list element 2 - the values
    cb.canvas.delete(tagStr)
    for i in range(items):
        # print(values[i])
        cb.canvas.create_text(x, y, text=str(values[i]), tag=tagStr, font=('Arial', cb.fontSize), anchor=NW)
        x = x + 50
    # last operation
    x = 550;    y = 300
    tagStr = "op"
    cb.canvas.delete(tagStr)
    cb.canvas.create_text(x, y, text="Last Action:  " + cb.operation, tag=tagStr,
                          font=('Arial', cb.fontSize), anchor=NW)


def addItem():
    global cb
    # print("add button clicked")
    item = cb.dataEntryValue.get()
    cb.dataEntryValue.set("")  # this clears the input box
    if item != "":
        success = newList.insertItem(item)
        if success:
            cb.operation = "add item " + item
        else:
            cb.operation = "failed to add item " + item
    else:
        cb.operation = "no item to add"

    drawListDisplay()


def deleteItem():
    # print("delete button clicked")
    item = cb.dataEntryValue.get()
    cb.dataEntryValue.set("")  # this clears the input box
    if item != "":
        success = newList.deleteItem(item)
        if success:
            cb.operation = "delete item " + item
        else:
            cb.operation = "failed to delete item " + item
    else:
        cb.operation = "no item to delete"
    drawListDisplay()


def resetList():  # empty the data list
    newList.resetStore(cb.storeSize)
    cb.operation = "empty the data list"
    drawListDisplay()


def configureList():  # set up the initial state of the store
    global cb
    global newList
    newList = LinkedList(cb.storeSize)

    addItems = ["Z", "Q", "R", "T", "E", "H", "Y"]
    deleteItems = ["T", "Q", "Y"]
    # create an item distribution that illustrates the linking of nodes
    for item in addItems:
        newList.insertItem(item)
    for item in deleteItems:
        newList.deleteItem(item)
    cb.operation = "example data and free lists"

    print("Initial condition of the store")
    newList.showAllNodes(newList.freePtr, "Free list: ")
    newList.showAllNodes(newList.startPtr, "Data list: ")
    newList.showPointers()
    newList.displayStore()


def main():

    global cb
    cb = ControlBlock()
    # root configuration
    root = Tk()
    root.title('Ordered Linked List Visualiser')
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

    visibleWidth = 1200; visibleHeight = 700  # a canvas of visible size vW x vH

    cb.canvas = Canvas(frame, bd=0, width=visibleWidth, height=visibleHeight,)

    cb.canvas.grid(row=0, column=0, sticky=N + S + E + W)

    # https: // www.geeksforgeeks.org / how - do - you - create - a - button - on - a - tkinter - canvas /
    # btn = Button(root, text='Exit!', width=40,height=5, bd='10', command=root.destroy)

    btnAdd = Button(root, text='Add', width=15, height=2, bd='5', command=addItem, font=('Arial', cb.fontSize))
    btnAdd.place(x=150, y=300)
    btnDelete = Button(root, text='Delete', width=15, height=2, bd='5', command=deleteItem, font=('Arial', cb.fontSize))
    btnDelete.place(x=150, y=400)

    btnReset = Button(root, text='Reset', width=15, height=2, bd='5', command=resetList, font=('Arial', cb.fontSize))
    btnReset.place(x=150, y=500)

    # data entry box
    # see here for input box https://www.geeksforgeeks.org/python-tkinter-entry-widget/
    cb.dataEntryValue = StringVar()
    dataEntryLabel = Label(root, text='Data Entry', font=('Arial', cb.fontSize, 'normal'))
    dataEntryLabel.place(x=150, y=210)
    dataEntry = Entry(root, textvariable=cb.dataEntryValue, width=10, font=('Arial', cb.fontSize, 'normal'))
    dataEntry.place(x=150, y=250)

    frame.pack()

    configureList()

    drawListDisplay()

    root.mainloop()


# end main()

if __name__ == "__main__":
    main()
