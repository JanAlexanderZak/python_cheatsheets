""" Binary Search
Given: Sorted array
Goal: Find target and its index
Time complexity: O(log n)
"""


def binary_search(_array: list, target: int) -> int:
    assert _array[0] < _array[-1]
    left_half = 0
    right_half = len(_array) - 1
    print("Array :", _array)

    while left_half <= right_half:
        middle = (left_half + right_half) // 2
        print("New mid: ", middle)

        if _array[middle] == target:
            print(f"Found target: {target} at index: {middle}")
            return middle
        elif target < _array[middle]:
            right_half = middle - 1
            print("New left_half:", _array[:right_half])
        else:
            left_half = middle + 1
            print("New right_half:", _array[left_half:])

    print("Target is not in array")
    return -1


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    binary_search(arr, 7)
