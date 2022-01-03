from typing import List


def find_first_occurrence(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    boundary = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            boundary = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return boundary


if __name__ == '__main__':
    arr = [int(x) for x in "4 6 7 7 7 20".split()]
    target = 8
    res = find_first_occurrence(arr, target)
    print(res)
