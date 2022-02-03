"""
sort file
"""

def insertion_sort(items):
    """ Insertion sort """

    size = items.size()


    for i in range(1, size):
        j = i
        while j > 0 and items.get(j) < items.get(j-1):
            temp = items.get(j)
            items.set(items.index_of(items.get(j)), items.get(j-1))
            items.set(items.index_of(items.get(j-1)), temp)
            j -= 1

    print(items.print_list())

def recursive_sort(items, n):
    """
    sort size
    """
    if n <= 1:
        return None

    recursive_sort(items, n-1)
    last = items.get(n-1)
    j = n-2

    while j >= 0 and items.get(j) > last:
        items.set(items.index_of(items.get(j+1)), items.get(j))
        j = j-1

    items.set(items.index_of(items.get(j+1)), last)

    return items.print_list()
