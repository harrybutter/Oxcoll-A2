"""
Made by hyunbin - Unordered Linked List
"""
from xml.sax.saxutils import prepare_input_source


class Node:
    def __init__(self):
        self.ptr = None
        self.data = "?"


class UnorderedLinkedlist:

    def __init__(self, size):
        self.freeptr = 0
        self.dataptr = None
        self.store = []
        for index in range(size):  # create store list in a fixed size
            self.store.append(Node())  # insert empty elements
            if index == size - 1:  # = the last element
                self.store[index].ptr = None  # set the pointer to None.
            else:
                self.store[index].ptr = index + 1  # set pointer to point the next node

    def display(self):
        print("---------------------------------------")
        print(f"DataPointer: {self.dataptr}")
        print(f"FreePointer: {self.freeptr}")
        store = []
        ptr = []
        free = []
        data = []
        dataptr = self.dataptr
        freeptr = self.freeptr
        for node in self.store:
            store.append(node.data)
            ptr.append(node.ptr)
        while dataptr is not None:
            data.append(self.store[dataptr].data)
            dataptr = self.store[dataptr].ptr
        while freeptr is not None:
            free.append(self.store[freeptr].data)
            freeptr = self.store[freeptr].ptr
        print(f"Store : {store}")
        print(f"Pointers : {ptr} \n")
        print(f"Data list : {data}")
        print(f"Free list : {free} \n")

    def insertNode(self, newitem):
        if self.freeptr is not None:  # which means that there is a free space available
            newNodeptr = self.freeptr  # get the first node from the free list
            self.store[newNodeptr].data = newitem  # store the data in that node
            self.freeptr = self.store[self.freeptr].ptr  # set the free list pointer to the next linked node (free)
            self.store[newNodeptr].ptr = self.dataptr  # set the pointer of the new node to the old data pointer
            self.dataptr = newNodeptr  # set the new data pointer to point the new node.
        else:
            print("<the list is full.>")

    def findNode(self, dataitem):  # returns pointer to node
        currentNodeptr = self.dataptr  # starts at the beginning of the list
        # while not end of the list and not found the item
        preNodeptr = None
        while currentNodeptr is not None and self.store[currentNodeptr].data != dataitem:
            preNodeptr = currentNodeptr
            currentNodeptr = self.store[currentNodeptr].ptr  # pointer of the next node

        return [currentNodeptr, preNodeptr]  # returns index of the item and previous item

    def deleteNode(self, dataitem):
        deletingNodeptr = self.findNode(dataitem)[0]  # the index of the dataitem
        preNodeptr = self.findNode(dataitem)[1]  # the index of the previous item
        if deletingNodeptr is not None:  # if the dataitem is in the data list,
            if deletingNodeptr == self.dataptr:  # if the first item of the datalist is to be deleted
                self.dataptr = self.store[self.dataptr].ptr  # dataptr is set to the index of 2nd item of datalist.
            else:
                # the pointer of the preNode is set to the pointer of the deleted node.
                self.store[preNodeptr].ptr = self.store[deletingNodeptr].ptr

            # adding the deleted node to the beginning of the free list
            # set the pointer of the deleted node to the current free pointer
            self.store[deletingNodeptr].ptr = self.freeptr
            self.freeptr = deletingNodeptr  # set the free pointer to the index of the deleted node.
        else:  # if the dataitem is not found in the list
            print(f"{dataitem} is not found in the Data list.")


def main():
    store = UnorderedLinkedlist(7)
    store.display()
    store.insertNode("hyunbin")
    store.insertNode("a oic")
    store.insertNode("zzz")
    store.insertNode("5")
    store.insertNode("spiderman")
    store.insertNode("blood")
    print(store.findNode("spiderman"), store.findNode("steven"))
    store.insertNode("IU")
    store.display()
    print(store.findNode("IU"))


if __name__ == "__main__":
    main()
