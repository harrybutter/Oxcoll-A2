'''
Made by hyunbin
'''
from xml.sax.saxutils import prepare_input_source


class Node:
    def __init__(self):
        self.ptr = None
        self.data = "?"


class Linkedlist:

    def __init__(self, size):
        self.size = size
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
            self.freeptr = self.store[self.freeptr].ptr  # set the free list pointer to the next linked node
            # find insertion point - alphabetical order
            thisnodeptr = self.dataptr  # searching from the beginning of the datalist
            preNodeptr = None  # in case we are inserting at the very front of the list.
            # searching through data list while not end of the list
            # and the item is smaller than the data value of the currently scanning node
            while thisnodeptr is not None and self.store[thisnodeptr].data < newitem:
                preNodeptr = thisnodeptr  # save this node
                thisnodeptr = self.store[thisnodeptr].ptr  # move on to the next linked node
            if self.dataptr is None or preNodeptr is None:  # which means the data list is empty
                # add the node at the start of the data list
                self.store[newNodeptr].ptr = self.dataptr  # the new node is set to None
                self.dataptr = newNodeptr  # the data pointer is set to the index of the new node
                # print(f"Data item {newitem} has been added at the beginning of the list.")
            else:  # insert new node between previous node and this node
                self.store[newNodeptr].ptr = self.store[preNodeptr].ptr  # new node's ptr <-- the preNode's ptr
                self.store[preNodeptr].ptr = newNodeptr  # preNode's ptr is now pointing the new node

                # print(f"Data {newitem} has been added to the list between {self.store[preNodeptr].data}
                # and {self.store[thisnodeptr].data}")
            return [newNodeptr, preNodeptr]
        else:
            print("<the list is full.>")
            return None

    def findNode(self, dataitem):  # returns pointer to node
        currentNodeptr = self.dataptr  # starts at the beginning of the list
        # while not end of the list and not found the item
        preNodeptr = None
        while currentNodeptr is not None and self.store[currentNodeptr].data != dataitem:
            preNodeptr = currentNodeptr
            currentNodeptr = self.store[currentNodeptr].ptr  # pointer of the next node

        return [currentNodeptr, preNodeptr]  # returns index of the item and previous item
        # returns None if item not found

    def deleteNode(self, dataitem):
        deletingNodeptr = self.findNode(dataitem)[0]  # the index of the dataitem
        preNodeptr = self.findNode(dataitem)[1]  # the index of the previous item
        if deletingNodeptr is not None:  # if the dataitem is in the data list,
            postNodeIndex = self.store[deletingNodeptr].ptr
            if deletingNodeptr == self.dataptr:  # if the first item of the datalist is to be deleted
                self.dataptr = self.store[self.dataptr].ptr  # dataptr is set to the index of 2nd item of datalist.
            else:
                # the pointer of the preNode is set to the pointer of the deleted node.
                self.store[preNodeptr].ptr = postNodeIndex

            # adding the deleted node to the beginning of the free list
            # set the pointer of the deleted node to the current free pointer
            self.store[deletingNodeptr].ptr = self.freeptr
            self.freeptr = deletingNodeptr  # set the free pointer to the index of the deleted node.
            return [deletingNodeptr, preNodeptr, postNodeIndex]
        else:  # if the dataitem is not found in the list
            print(f"{dataitem} is not found in the Data list.")
            return None


def main():
    store = Linkedlist(7)
    store.display()
    store.insertNode("hyunbin")
    store.insertNode("zzz")
    store.insertNode("5")
    store.insertNode("spiderman")
    print(store.findNode("spiderman"), store.findNode("steven"))
    store.insertNode("naruto")
    store.insertNode("sasuke")
    store.insertNode("IU")
    store.display()


if __name__ == "__main__":
    main()

# Store : ['hyunbin', 'zzz', '5', 'spiderman', 'naruto', 'sasuke', 'IU']
# Pointers : [4, None, 6, 1, 5, 3, 0]
