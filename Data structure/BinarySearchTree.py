"""Binary Tree Search Class"""


class Node:
    def __init__(self, data):
        self.data = data
        self.leftPtr = None
        self.rightPtr = None


class BinaryTreeSearch:
    def __init__(self, size):
        self.size = size
        self.store = []
        for i in range(size):
            self.store.append(Node(None))
            self.store[i].leftPtr = i + 1
        self.store[size - 1].leftPtr = None  # last node of the list
        self.rootPtr = None
        self.freePtr = 0

    def insertNode(self, newItem):
        if self.freePtr is not None:  # if there is a space
            # take a node from the free list, store data item, set null pointer
            newNodePtr = self.freePtr
            self.freePtr = self.store[self.freePtr].leftPtr
            self.store[newNodePtr].data = newItem
            self.store[newNodePtr].leftPtr = self.store[newNodePtr].rightPtr = None
            # check if the store is empty
            if self.rootPtr is None:  # if it is, insert the new node at root.
                self.rootPtr = newNodePtr
            else:  # find insertion point
                turnLeft = None
                preNodeptr = None
                thisNodeptr = self.rootPtr  # start at the root of the tree
                while thisNodeptr is not None:  # while not a leaf node
                    preNodeptr = thisNodeptr  # store this node
                    if self.store[thisNodeptr].data > newItem:  # if item is larger than the data
                        turnLeft = True
                        # move left
                        # current node's left pointer is now stored in ThisNodePtr.
                        thisNodeptr = self.store[thisNodeptr].leftPtr
                    else:
                        turnLeft = False
                        # move right
                        # current node's right pointer is now stored in thisNodePtr.
                        thisNodeptr = self.store[thisNodeptr].rightPtr
                if turnLeft is True:
                    self.store[preNodeptr].leftPtr = newNodePtr
                else:
                    self.store[preNodeptr].rightPtr = newNodePtr
            return newNodePtr
        else:
            print("The store is full")
            return None

    def findNode(self, searchItem):
        thisNodeptr = self.rootPtr  # start from the root
        # while where is a pointer to follow and search item not found
        while thisNodeptr is not None and self.store[thisNodeptr].data is not searchItem:
            if self.store[thisNodeptr].data > searchItem:  # follow left pointer
                thisNodeptr = self.store[thisNodeptr].leftPtr
            else:  # follow to right
                thisNodeptr = self.store[thisNodeptr].rightPtr
        return thisNodeptr  # None will be returned if item is not found
