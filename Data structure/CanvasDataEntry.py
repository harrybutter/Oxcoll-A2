# a demonstration of how to create and use a Tkinter canvas
#  draw lines, squares and circles on the canvas
#  add text to the canvas
#  update text on the canvas at specified intervals

try:
    from Tkinter import *
except:
    from tkinter import *


def doStep(value):
    print("value entered is ",value)
    
    
if __name__ == "__main__":
    
    root = Tk()
    root.title('Canvas Data Entry Demonstration')

    # Values of width and height are pixels
    # (0,0) is the top left corner of the canvas
    #
    canvas = Canvas(root, width = 500, height = 500, bg = "white")
    canvas.pack() 
    
    fontSize = 10
    # see here for input box https://www.geeksforgeeks.org/python-tkinter-entry-widget/
    dataEntryValue = StringVar()
    dataEntryLabel = Label(root, text='Data Entry', font=('Arial', fontSize, 'normal'))
    dataEntryLabel.place(x=150, y=210)
    dataEntry = Entry(root, textvariable=dataEntryValue, width=10, font=('Arial', fontSize, 'normal'))
    dataEntry.place(x=150, y=250)
    
    # https://www.geeksforgeeks.org/how-do-you-create-a-button-on-a-tkinter-canvas/
    btnLeft = Button(root, text='Step', width=15, height=2, bd='5', command= lambda:doStep(dataEntryValue.get()),
                     font=('Arial', 10))
    btnLeft.place(x=50, y=300)
       
    
    
    root.mainloop()
