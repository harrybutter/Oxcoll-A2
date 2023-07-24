"""
Ordered Linked List GUI
"""

import ordered_linked_lists
from tkinter import *


def update_rectangle(index, data, ptr, colour):
    yLocation = 100 + 50 * index
    cv.create_rectangle((300, yLocation, 400, yLocation + 50), fill=colour)
    cv.create_rectangle((400, yLocation, 470, yLocation + 50), fill=colour)
    if data is not None:
        cv.create_text(350, yLocation + 25, text=data, font=("Arial", 10))
        cv.create_text(435, yLocation + 25, text=ptr, font=("Arial", 10))


def add():
    data = value.get()
    indexes = llist.insertNode(data)  # [location of the new data node, previous node]
    index = indexes[0]
    preIndex = indexes[1]
    if index is not None:  # list is not full
        ptr = llist.store[index].ptr
        print(ptr, preIndex)
        if ptr is None:
            ptr = "None"
        if preIndex is None:  # the list is empty
            update_rectangle(index, data, ptr, "MediumOrchid1")  # update the new node ONLY
        else:
            update_rectangle(index, data, ptr, "MediumOrchid1")  # update the new node
            # update the pointer of the previous node
            update_rectangle(preIndex, llist.store[preIndex].data, index, "MediumOrchid1")


def remove(data):
    itemRemove = data.get()
    deletingNode = llist.deleteNode(itemRemove)
    if deletingNode is not None:  # if the item is found
        deletingNodeptr = deletingNode[0]
        preNodeptr = deletingNode[1]
        postNodeIndex = deletingNode[2]
        ptr = llist.store[deletingNodeptr].ptr
        if preNodeptr is None:  # first item is removed
            update_rectangle(deletingNodeptr, itemRemove, ptr, "SeaGreen1")
        else:
            update_rectangle(deletingNodeptr, itemRemove, ptr, "SeaGreen1")
            update_rectangle(preNodeptr, llist.store[preNodeptr].data, postNodeIndex, "MediumOrchid1")
    else:
        print("Item Not found. - GUI")


if __name__ == "__main__":
    llist = ordered_linked_lists.Linkedlist(7)
    root = Tk()
    root.title("Linked List GUI")
    cv = Canvas(root, width=1000, height=600, bg="white")
    cv.pack()

    cv.create_text(350, 80, text="Elements", font=("Arial", 10))
    cv.create_text(435, 80, text="Pointers", font=("Arial", 10))
    for i in range(llist.size):
        y = 100+50*i
        cv.create_rectangle((300, y, 400, y+50), fill="SeaGreen1")
        cv.create_rectangle((400, y, 470, y+50), fill="SeaGreen1")
        cv.create_text(285, y+25, text=i, font=("Arial", 10))

    # Display settings
    value = StringVar()
    valueLabel = Label(root, text='Data Entry', font=('Arial', 10, 'normal'))
    valueLabel.place(x=50, y=150)
    entry = Entry(root, textvariable=value, width=15, font=('Arial', 10, 'normal'))
    entry.place(x=120, y=150)
    addBtn = Button(root, text='Add', width=12, height=1, bd='3', command=lambda: add(),
                    font=('Arial,', 8))
    addBtn.place(x=100, y=180)
    deleteBtn = Button(root, text='Delete', width=12, height=1, bd='3', command=lambda: remove(value),
                       font=('Arial,', 8))
    deleteBtn.place(x=100, y=210)
    root.mainloop()

