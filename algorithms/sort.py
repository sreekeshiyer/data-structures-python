a = [1, 6, 3, 2, 8, 2, 4]


def bubble_sort(a: list[int], l=len(a)):
    '''
    Bubble Sort
    '''
    for i in range(l):
        for j in range(l-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


def selection_sort(a: list[int]):
    '''
    Selection Sort
    '''
    length = len(a)

    for i in range(length):
        min = i
        smallest = a[i]
        for j in range(i+1, length):
            if a[j] < a[min]:
                min = j

        a[i], a[min] = a[min], smallest

    return a
