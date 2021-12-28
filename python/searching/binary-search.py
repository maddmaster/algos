from typing import List


def binary_search_iterative(items: List[str], search_for: str) -> int:
    start = 0
    end = len(items)

    print(items)

    while start <= end:
        mid = (start + end) // 2

        if search_for == items[mid]:
            return mid

        if search_for > items[mid]:
            start = mid + 1
        else:
            end = mid - 1

        print("{}, {}, {}".format(start, end, mid))

    return - 1


def main():
    str = "ABCDEFGHIJ"
    position = binary_search_iterative(list(str), "H")
    print(position)


if __name__ == '__main__':
    main()
