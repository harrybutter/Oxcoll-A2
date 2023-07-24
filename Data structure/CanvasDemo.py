# a demonstration of how to create and use a Tkinter canvas
#  draw lines, squares and circles on the canvas
#  add text to the canvas
#  update text on the canvas at specified intervals

try:
    from Tkinter import *
except:
    from tkinter import *

# importing strftime function to retrieve system time 
from time import strftime


def updateTime(canvas, root):  # refresh the time display
    canvas.delete("timedisplay")  # erase previous value
    string = strftime('%H:%M:%S')
    canvas.create_text(450, 50, text=string, tag="timedisplay")
    root.after(1000, updateTime, canvas, root)  # set up the callback after 1000ms have elapsed


if __name__ == "__main__":
    root = Tk()
    root.title('Canvas Demonstration')

    # Values of width and height are pixels
    # (0,0) is the top left corner of the canvas
    #
    canvas = Canvas(root, width=500, height=500, bg="white")
    canvas.pack()

    canvas.create_line((0, 0, 100, 100), width=1, fill="black")
    # first argument is a tuple in a form (x1, y1, x2, y2)
    # x1, y1 coordinates of the first point
    # x2, y2 coordinate of the second point
    # width - number of pixels
    # fill - color
    # (there are many more options but these are the essential ones)

    canvas.create_rectangle((200, 200, 400, 400), width=1, fill="red")
    # first argument is a tuple in a form (x1, y1, x2 , y2)
    # x1, y1 coordinates of the TOP-LEFT corner of the rectangle
    # x2, y2 coordinates of the BOTTOM-RIGHT corner of the rectangle
    # width - number of pixels
    # fill - color
    diameter = 200
    originX = 100
    originY = 100
    canvas.create_oval(originX, originY, originX + diameter, originY + diameter, width=6,
                       outline='blue')  # circle is a special case of an ellipse
    canvas.create_text(250, 50, text="testing text")

    root.after(0, updateTime(canvas, root))  # immediate time display

    root.mainloop()
