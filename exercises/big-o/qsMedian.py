from random import shuffle

# 1000 items: 4 loops, best of 5: 22.7 msec per loop

def main():
    listToOrder = generateList()
    unorderedList = shuffleList(listToOrder)
    quickSort(unorderedList)


def generateList(size=1000):
    return list(range(size))


def shuffleList(listToOrder):
    shuffle(listToOrder)
    return listToOrder


def getPivot(alist):
    lengthOfItemsList = len(alist) - 1
    halfsize = round((lengthOfItemsList / 2))
    first = alist[0]
    middle = alist[halfsize]
    last = alist[lengthOfItemsList]
    median = round((first + middle + last) / 3)
    return alist[median]


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(array, first, last):
    pivotvalue = getPivot(array)
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and array[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while array[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = array[leftmark]
            array[leftmark] = array[rightmark]
            array[rightmark] = temp

    temp = array[first]
    array[first] = array[rightmark]
    array[rightmark] = temp
    return rightmark

if __name__ == "__main__":
    main()
