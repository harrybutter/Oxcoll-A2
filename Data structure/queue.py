"""Queue class"""


class Queue:
    def __init__(self, size):
        self.size = size
        self.array = []
        for _ in range(size):
            self.array.append(None)
        self.headPtr = 0
        self.tailPtr = -1

    def add(self, value):
        if self.tailPtr == self.size - 1:  # if the ptr is the end, turn into -1
            # so that it can be compared with the next value
            self.tailPtr = 0
        else:
            self.tailPtr += 1
        if self.tailPtr == self.headPtr and self.array[self.tailPtr] is not None:  # the queue is full
            # print('the queue is full')
            return "Queue Full"
        else:
            self.array[self.tailPtr] = value
            # print('added')
            return True

    def remove(self):
        data = self.array[self.headPtr]
        if self.array[self.headPtr] is None:  # the queue is empty
            # print('the queue is empty')
            return "Queue Empty"
        else:
            # print("popped")
            self.array[self.headPtr] = None
            if self.headPtr == self.size - 1:  # if the ptr is pointing the last value, loop to the beginning.
                self.headPtr = 0
            else:
                self.headPtr += 1
            return data

    def display(self):
        head = self.headPtr
        tail = self.tailPtr
        contents = []
        while head != tail:
            print(head)
            if head == self.size-1:  # wrap around
                head = 0
            else:
                head += 1
            contents.append(self.array[head])
        return contents


def main():
    queue1 = Queue(5)
    queue1.add(3)
    queue1.add(5)
    queue1.add(31)
    queue1.remove()
    queue1.remove()
    print(queue1.array)


if __name__ == "__main__":
    main()
