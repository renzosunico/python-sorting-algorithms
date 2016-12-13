def bubble_sort(unsorted):
    for i in range(0, len(unsorted)):
        for j in range(0, len(unsorted), 1):
            if j+1 < len(unsorted):
                if unsorted[j+1] < unsorted[j]:
                    unsorted[j+1], unsorted[j] = unsorted[j], unsorted[j+1]
