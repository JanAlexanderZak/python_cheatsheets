""" Selection Sort
Find minimum and put at beginning
Time complexity: O(n^2)
"""


def selection_sort(_array: list) -> list:
    for i in range(len(_array) - 1):
        index = i

        for j in range(i + 1, len(_array)):
            # find next lowest value and set index at this point
            if _array[j] < _array[index]:
                index = j

        _array[i], _array[index] = _array[index], _array[i]
        print(_array)
    return _array


if __name__ == '__main__':
    arr = [1, 3, 2, 4, 5, 8, 7, 9]
    selection_sort(arr)

