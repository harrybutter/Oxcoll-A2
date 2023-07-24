# This code based on the pseudocode from Langfield & Duddell Chapter 23
# This is an ORDERED linked List

# Use Python's None value to indicate a null pointer

class Node():
    # node for a single linked list
    def __init__(self, data):
        self.data = data  # data value
        self.next = None  # pointer value


# END-CLASS

class LinkedList():
    def __init__(self, size):
        # PROCEDURE InitialiseList
        self.store = []
        self.startPtr = None  # empty data list
        self.freePtr = 0  # first node in the free list
        self.size = size

        for i in range(self.size):  # create a list entry for each node
            node = Node(10 + i)
            self.store.append(node)
        self.resetStore(self.size)

    def resetStore(self, numRows):  # sets the store to an empty data list
        for i in range(numRows):  # initialise the nodes as items in the free list
            self.store[i].next = i + 1
            self.store[i].data = "?"  # dummy data

        self.store[numRows - 1].next = None  # end of free list
        self.startPtr = None  # empty data list
        self.freePtr = 0  # first node in the free list

    def insertItem(self, newItem):  # InsertNode()
        success = True  # assume insert will be successful
        if self.freePtr is not None:  # space available for the new item
            newNodePtr = self.freePtr
            self.store[newNodePtr].data = newItem
            self.freePtr = self.store[self.freePtr].next

            # find the insertion point for the new item
            thisNodePtr = self.startPtr
            prevNodePtr = None  # to allow a new item to be inserted at start of an existing list

            while thisNodePtr is not None and self.store[thisNodePtr].data < newItem:
                prevNodePtr = thisNodePtr
                thisNodePtr = self.store[thisNodePtr].next

            if self.startPtr is None or prevNodePtr is None:  # insert item at start of list (NM modification)
                self.store[newNodePtr].next = self.startPtr
                self.startPtr = newNodePtr
            else:  # insert between previous node and this node
                self.store[newNodePtr].next = self.store[prevNodePtr].next
                self.store[prevNodePtr].next = newNodePtr
        else:
            print("insert failed: no room in store")
            success = False
        return success

    def findItem(self, item):  # search the data list for the specified item
        ptr = self.startPtr
        while ptr is not None and self.store[ptr].data != item:
            ptr = self.store[ptr].next

        if ptr is None:
            print("item not found")
        else:
            print("item ", item, " is at index ", ptr)

        return ptr  # returns the store index of the item or None if item not found

    def deleteItem(self, item):
        success = True  # assume successful delete
        thisNodePtr = self.startPtr
        # WHILE not end of list AND item not found
        while thisNodePtr is not None and self.store[thisNodePtr].data != item:
            prevNodePtr = thisNodePtr
            thisNodePtr = self.store[thisNodePtr].next

        if thisNodePtr is not None:  # node exists in the list
            # unlink the node from the data list
            if thisNodePtr is self.startPtr:  # delete the first node
                self.startPtr = self.store[self.startPtr].next
            else:
                self.store[prevNodePtr].next = self.store[thisNodePtr].next  # NM modification
            # add the deleted node to the free list
            self.store[thisNodePtr].next = self.freePtr
            self.freePtr = thisNodePtr
        else:
            print("delete failed: item ", item, " not in list")
            success = False
        return success

    def showAllNodes(self, start, label):  # display all nodes from the specified list
        ptr = start
        items = 0
        print(label, end="")
        while ptr is not None:
            print(self.store[ptr].data, "  ", end="")
            ptr = self.store[ptr].next
            items += 1
        print("  ", items, "items")

    # methods from here on are for displaying the store and lists
    def displayStore(self):  # display the entire store for diagnostic purposes
        print("Store contents:")
        print("index \tdata \tpointer")
        # display values of data and free pointers
        for i in range(len(self.store)):
            print(" ", i, "\t ", self.store[i].data, " \t ", self.store[i].next)

    def showPointers(self):  # display the pointers for the data list and the free list
        print("Pointers: startPtr ", self.startPtr, " freePtr ", self.freePtr)

    def getPointers(self):
        return self.startPtr, self.freePtr

    def getStore(self):  # return lists of the data and next values
        data = []
        next = []
        for i in range(len(self.store)):
            data.append(str(self.store[i].data))
            if self.store[i].next is None:
                next.append(str(self.store[i].next))  # do convert this to string
            else:
                next.append(self.store[i].next)  # don't convert this to string
        return data, next

    # return a list of all the data values for either "data" or "free" lists
    def getListData(self, listID):
        if listID == "data":
            ptr = self.startPtr
        else:
            ptr = self.freePtr
        results = []
        while ptr is not None:
            results.append(self.store[ptr].data)
            ptr = self.store[ptr].next
        return results

    # return a list of all the pointer values for either "data" or "free" lists
    def getListPtrs(self, listID):
        if listID == "data":
            ptr = self.startPtr
        else:
            ptr = self.freePtr
        results = []
        results.append(ptr)
        while ptr is not None:
            if self.store[ptr].next is not None:
                results.append(self.store[ptr].next)
            ptr = self.store[ptr].next
        return results

# end class
