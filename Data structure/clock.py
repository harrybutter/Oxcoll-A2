"""Clock demonstration"""

from tkinter import *
import numpy as np


class ControlBlock:  # Global variables
    def __init__(self):
        # display attributes
        self.canvas = 0
        self.fontSize = 8
        self.title = "GUI Template"
        # version number
        self.verStr = "1.0"
        # author
        self.author = "Hyunbin Jang"
        self.date = "Jan 2023"
        self.angle = 2 * np.pi / 12


global cb  # ControlBlock


class Clock:
    global cb

    def __init__(self, cv, city, timediff, x, y):
        self.city = city
        self.timediff = timediff

        for i in range(12):
            M = np.array([
                [np.cos(cb.angle * i), -np.sin(cb.angle * i)],
                [np.sin(cb.angle * i), np.cos(cb.angle * i)]
            ])
            twelve = np.array([0, -200])
            newPoint = np.dot(twelve, M)
            x1 = newPoint[0] + 500
            y2 = newPoint[1] + 300
            cv.create_text(x1 + 35, y2 + 35, text=i)
        cv.create_oval((x, y, x + 300, y + 300), width=4)
        cv.create_line((x, y, x+10, y+10, x+20, y+40), width=3)



def main():
    global cb
    cb = ControlBlock()
    root = Tk()
    root.title(cb.title)
    cv = Canvas(root, width=1000, height=600, bg="white")
    cv.pack()

    london = Clock(cv, "london", 0, 70, 100)

    root.mainloop()


if __name__ == "__main__":
    main()
