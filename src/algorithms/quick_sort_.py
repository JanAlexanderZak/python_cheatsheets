""" Quick Sort
Unsorted array
Iterate over pivot point
split in halves and repeat
Time complexity: O(n^2)
"""


def quick_sort(_array):
    n = len(_array)

    if n <= 1:
        return _array

    pivot = _array.pop()

    items_greater, items_lower = [], []

    [items_greater.append(item) if (item > pivot) else items_lower.append(item) for item in _array]
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


if __name__ == '__main__':
    arr = [4, 3, 1, 5, 2, 7, 8]
    print(quick_sort(arr))
