def bubble_sort(unsorted):
    for i in range(0, len(unsorted)):
        for j in range(0, len(unsorted), 1):
            if j+1 < len(unsorted):
                if unsorted[j+1] < unsorted[j]:
                    unsorted[j+1], unsorted[j] = unsorted[j], unsorted[j+1]


def insertion(unsorted):
    for index in range(1, len(unsorted)):
        currentValue = unsorted[index]
        position = index

        while position > 0 and unsorted[position-1] > currentValue:
            unsorted[position] = unsorted[position-1]
            position = position -1
        unsorted[position] = currentValue


def quicksort(unsorted):
    if len(unsorted) > 1:
        pivot = unsorted[0]
        left = []
        middle = []
        right = []
        for val in unsorted:
            if val < pivot:
                left.append(val)
            elif val == pivot:
                middle.append(val)
            elif val > pivot:
                right.append(val)
        left = quicksort(left)
        middle = quicksort(middle)
        right = quicksort(right)
        return left + middle + right
    else:
        return unsorted
    
