""" Merge Sort
-> Divide and conquer
1. Divide in two halfes until pairs of 2, recursive function
2. Merge them together
Time complexity: O(n log n)
"""


def merge_sort(_array):
    # Escape from recursion
    if len(_array) < 2:
        return _array

    # Divide array un two halves
    mid = len(_array) // 2
    left_half = merge_sort(_array[:mid])
    right_half = merge_sort(_array[mid:])

    i = j = k = 0

    # Instantiate empty arrays
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            _array[k] = left_half[i]
            i += 1
        else:
            _array[k] = right_half[j]
            j += 1
        k += 1

    # Check for each element
    while i < len(left_half):
        _array[k] = left_half[i]
        i += 1
        k += 1

    # Check for each element
    while j < len(right_half):
        _array[k] = right_half[j]
        j += 1
        k += 1

    return _array


if __name__ == '__main__':
    arr = [4, 3, 1, 5, 2, 7, 8]
    print(merge_sort(arr))
