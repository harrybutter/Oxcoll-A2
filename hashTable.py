"""Hash table simulator"""


class Record:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f'Customer ID: {self.id}')
        print(f'Customer name: {self.name}')


class HashTable:

    def __init__(self, tablesize):
        self.tablesize = tablesize
        self.hashTable = []
        self.collisions = 0
        for _ in range(tablesize):
            self.hashTable.append(Record(None, ''))

    def hash(self, key):  # returns storage location
        return key % self.tablesize

    def getCollisions(self):
        return self.collisions

    def insert(self, newRecord):
        index = self.hash(newRecord.id)
        firstindex = index
        print("Inserting index:", index)
        if self.hashTable[index].id is not None:  # Increment collision counter
            self.collisions += 1
        while self.hashTable[index].id is not None:  # record is full
            index += 1
            if index == firstindex:
                print("The hash table is full")
                return None
            if index > self.tablesize:
                index = 0
        # now index indicates an empty slot
        self.hashTable[index] = newRecord

    def findRecord(self, searchKey):
        index = self.hash(searchKey)
        print("find index: ", index)
        firstIndex = index
        while self.hashTable[index].id != searchKey and self.hashTable[index].id is not None:
            index += 1
            if index == firstIndex:
                print("The hash table is full, and the record is not found.")
                return None
            if index > self.tablesize:
                index = 0
        if self.hashTable[index].id is not None:
            return self.hashTable[index].name  # record found
        else:
            print('Not found')
            return None  # Not found


def main():
    ht = HashTable(10)
    ht.insert(Record(45876, 'Hyunbin'))
    ht.insert(Record(32390, 'Jang'))
    ht.insert(Record(95612, 'Sara'))
    ht.insert(Record(64636, 'Steven'))
    ht.insert(Record(23467, 'IU'))
    print(ht.findRecord(23467))
    print(ht.getCollisions())


if __name__ == '__main__':
    main()
