"""Binary Search
Given: Sorted array
Goal: Find target and its index
Time comlexity: O(n)
"""


def linear_search(_array: list, target: int, _sorted=True) -> int:
    n = len(_array)
    if _sorted:
        for i in range(0, n):
            if _array[i] == target:
                print(f"Found target: {target} at index {i}")
                return i
            if _array[i] > target:
                break
        print("Target not found in list")
        return -1

    else:
        for i in range(0, n):
            if _array[i] == target:
                print(f"Found target: {target} at index {i}")
                return i

        return -1


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(linear_search(arr, 10, _sorted=True))
