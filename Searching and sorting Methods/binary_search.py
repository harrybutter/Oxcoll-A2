"""Binary search algorithm"""


def binarySearch(list, element):
    print('binarySearch')
    list = sorted(list)
    start = 0
    end = len(list)
    midp = (start + end) // 2
    while list[midp] != element:
        if list[midp] > element:
            end = midp
            print(f"{list} start:{start} end:{end}")
        elif list[midp] < element:
            start = midp + 1
            print(f"{list} start:{start} end:{end}")
        midp = (start + end) // 2
        if (end - start) <= 1 and list[midp] != element:
            print("Item not in the list.")
            return None
    return midp


# alternative
def binarySearch2(list, element):  # using the recursion of the function binarySearch2
    print('binarySearch2')
    list.sort()
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint] == element:
            return midpoint
        else:
            if element < list[midpoint]:
                return binarySearch2(list[:midpoint], element)
            else:
                return binarySearch2(list[midpoint+1:], element)


def main():
    list = [1, 3, 6, 7, 4, 8, 55, 65, 368, 72, 88, 4]
    print(binarySearch2(list, 99))


if __name__ == "__main__":
    main()
