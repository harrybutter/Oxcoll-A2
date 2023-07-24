# an example of how to create and use a Tkinter canvas
#  draw lines, squares and circles on the canvas
#  add text to the canvas
#  update text on the canvas at specified intervals

try:
    from Tkinter import *
except:
    from tkinter import *

# importing strftime function to retrieve system time 
from time import strftime

global fillChoice
fillColours = ["red", "green", "blue"]


def updateTime(canvas, root):  # refresh the time display and colour of rectangle
    global fillChoice, fillColours
    canvas.delete("timedisplay")  # erase previous value
    string = strftime('%H:%M:%S')
    secs = int(string[-2:])
    if secs % 2 == 0:
        canvas.delete("rectangle")
        fillColour = fillColours[fillChoice]
        fillChoice = (fillChoice + 1) % len(fillColours)
        canvas.create_rectangle((200, 200, 400, 400), tag="rectangle", width=1,
                                fill=fillColour)

    canvas.create_text(450, 50, text=string, tag="timedisplay")
    root.after(1000, updateTime, canvas, root)
    # set up the callback each time with interval of 1000msec


if __name__ == "__main__":
    root = Tk()
    root.title('Canvas Demonstration')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    print("screen size: width ", screen_width, "height ", screen_height)

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
    # (there are more stuff but i don't think we will hardly ever need anything else)

    canvas.create_rectangle((200, 200, 400, 400), width=1, fill="red")
    # first argument is a tuple in a form (x1, y1, x2 , y2)
    # x1, y1 coordinates of the TOP-LEFT corner of the rectangle
    # x2, y2 coordinates of the BOTTOM-RIGHT corner of the rectangle
    # width - number of pixels
    # fill - color
    global fillChoice
    fillChoice = 0
    diameter = 200
    originX = 100
    originY = 100
    canvas.create_oval(originX, originY, originX + diameter,
                       originY + diameter)  # circle is a special case of an ellipse
    canvas.create_text(250, 50, text="testing text")

    root.after(0, updateTime, canvas, root)  # immediate time display

    root.mainloop()
