from typing import List


def find_boundary(arr: List[bool]) -> int:
    left, right = 0, len(arr) - 1
    boundary = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid]:
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary


if __name__ == '__main__':
    arr = [x == "true" for x in "false false true true true".split()]
    print(arr)
    res = find_boundary(arr)
    print(res)
