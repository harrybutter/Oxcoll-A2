"""
Insertion sorting algorithm
04/10/2022
"""


def insertion_sort(array):
    # for i in range(1, len(array)):
    #     ItemToBeInserted = array[i]  # item to be inserted
    #     currentItem = i - 1  # the last item in the sorted part of the list
    #     if array[currentItem] > ItemToBeInserted:
    #         while currentItem >= 0 and array[currentItem] > ItemToBeInserted:
    #             #  array[place+1], array[place] = array[place], array[place+1]
    #             temp = array[currentItem+1]
    #             array[currentItem+1] = array[currentItem]
    #             array[currentItem] = temp
    #         ItemToBeInserted = array[currentItem+1]
    for i in range(1, (len(array))):
        print(array)
        itemToBeSorted = array[i]
        while i > 0 and itemToBeSorted < array[i-1]:
            array[i] = array[i-1]
            array[i-1] = itemToBeSorted
            i -= 1

    return array


array = [2, 15, 36, 8, 9, 4, 8, 233, 61, 1]
print(insertion_sort(array))
