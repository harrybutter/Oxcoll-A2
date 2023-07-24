"""Queue GUi"""

from tkinter import *
from queues import Queue
import numpy as np

QUEUE_SIZE = 10


def drawCircle(cv, index, colour, text):
    rotation = 2 * np.pi / QUEUE_SIZE
    firstCentre = np.array([0, -200])
    M = np.array([
        [np.cos(rotation * index), -np.sin(rotation * index)],
        [np.sin(rotation * index), np.cos(rotation * index)]
    ])
    newCentre = np.dot(firstCentre, M)
    x = newCentre[0] + 500
    y = newCentre[1] + 300
    cv.create_oval((x, y, x + 70, y + 70), fill=colour)
    cv.create_text(x+35, y+35, text=text)


def add(cv, queue, value):
    data = value.get()
    result = queue.push(data)
    k = queue.tailPtr
    if result is not True:
        print(result)
    else:
        drawCircle(cv, k, 'green', data)
    updatePtr(cv,queue)


def remove(cv,queue):
    data = queue.pop()
    n = queue.headPtr - 1
    if data == "Queue underflow":
        print(data)
    else:
        drawCircle(cv,n, 'skyblue', '')
        print(data, 'removed')
    updatePtr(cv,queue)


def display(queue):
    print(queue.array)


def updatePtr(cv, queue):
    cv.delete("headPtr")
    cv.delete("tailPtr")
    cv.create_text(525, 290, text=f"Head Pointer: {queue.headPtr}", tag='headPtr')
    cv.create_text(525, 305, text=f"Tail Pointer: {queue.tailPtr}", tag='tailPtr')


def main():
    queue = Queue(QUEUE_SIZE) 
    root = Tk()
    root.title("Queue GUI")
    cv = Canvas(root, width=800, height=700, bg="white")
    cv.pack()

    for i in range(QUEUE_SIZE):  
        # cv.create_rectangle((100 + 50 * i, 100, 150 + 50 * i, 200), fill="skyblue")
        # rotation by appropriate angle
        drawCircle(cv,i, "skyblue", "")
        # setting up indexes
        angle = 2 * np.pi / QUEUE_SIZE
        centre = np.array([0, -250])
        M = np.array([
            [np.cos(angle * i), -np.sin(angle * i)],
            [np.sin(angle * i), np.cos(angle * i)]
        ])
        c = np.dot(centre, M)
        x1 = c[0] + 500
        y2 = c[1] + 300
        cv.create_text(x1 + 35, y2 + 35, text=i)    

    value = StringVar()
    valueLabel = Label(root, text='Data Entry', font=('Arial', 10, 'normal'))
    valueLabel.place(x=100, y=150)
    entry = Entry(root, textvariable=value, width=25, font=('Arial', 10, 'normal'))
    entry.place(x=170, y=150)
    addBtn = Button(root, text='Add', width=12, height=1, bd='3', command=lambda: add(cv,queue,value),
                    font=('Arial,', 8))
    addBtn.place(x=100, y=180)
    removeBtn = Button(root, text='Remove', width=12, height=1, bd='3', command=lambda: remove(cv,queue),
                       font=('Arial,', 8))
    removeBtn.place(x=100, y=210)
    displayBtn = Button(root, text='Display', width=12, height=1, bd='3', command=lambda: display(queue),
                        font=('Arial,', 8))
    displayBtn.place(x=100, y=240)

    root.mainloop()


if __name__ == "__main__":
    main()
