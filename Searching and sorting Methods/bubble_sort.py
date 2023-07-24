"""bubble sort algorithm"""


# string = input()
def bubble_sort(array):
    swap = True
    for i in range(len(array)):
        if not swap:  # the array is already sorted
            return array
        swap = False
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap = True
    return array


array = [1, 15, 36, 8, 9, 4, 8, 33, 61]
print(bubble_sort(array))
