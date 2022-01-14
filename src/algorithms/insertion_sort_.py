""" Inertion Sort
Unsorted array
compare pairwise and move greater number to right
Time complexity: O(n)
"""


def insertion_sort(_array):
    n = len(_array)

    for i in range(n):
        key = _array[i]
        j = i - 1
        while j >= 0 and key < _array[j]:
            _array[j + 1] = _array[j]
            j -= 1
        _array[j + 1] = key
    return _array


if __name__ == '__main__':
    arr = [4, 3, 1, 5, 2, 7, 8]
    print(insertion_sort(arr))
