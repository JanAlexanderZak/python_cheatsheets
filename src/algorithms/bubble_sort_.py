""" Bubble Sort
Unsorted array
compare pairwise and move greater number to right
Time complexity: O(n log n)
"""


def bubble_sort(_array):
    n = len(_array) - 1

    for i in range(n):
        for j in range(0, n - i - 1):
            # Move greater element to right
            if _array[j] > _array[j + 1]:
                _array[j], _array[j + 1] = _array[j + 1], _array[j]
    return _array


if __name__ == '__main__':
    arr = [4, 3, 1, 5, 2, 7, 8]
    print(bubble_sort(arr))
