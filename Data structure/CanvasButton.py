# a demonstration of how to create and use a Tkinter canvas
#  draw lines, squares and circles on the canvas
#  add text to the canvas
#  update text on the canvas at specified intervals

try:
    from Tkinter import *
except:
    from tkinter import *


def doShiftLeft():
    print("shifting left")


if __name__ == "__main__":
    root = Tk()
    root.title('Canvas Demonstration')

    # Values of width and height are pixels
    # (0,0) is the top left corner of the canvas
    #
    canvas = Canvas(root, width=500, height=500, bg="white")
    canvas.pack()

    canvas.create_line((0, 0, 100, 100), width=1, fill="black")
    canvas.create_rectangle((200, 200, 400, 400), width=1, fill="blue")
    diameter = 200
    originX = 100
    originY = 100
    canvas.create_oval(originX, originY, originX + diameter, originY + diameter, width=6,
                       outline='blue')  # circle is a special case of an ellipse
    canvas.create_text(250, 50, text="testing text")

    # https://www.geeksforgeeks.org/how-do-you-create-a-button-on-a-tkinter-canvas/
    btnLeft = Button(root, text='<   Shift Left', width=15, height=2, bd='5', command=lambda: doShiftLeft(),
                     font=('Arial', 10))
    btnLeft.place(x=50, y=300)

    root.mainloop()
