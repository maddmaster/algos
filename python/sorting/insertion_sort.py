from typing import List


def insertion_sort(unsorted: List[int]) -> List[int]:
    for i, entry in enumerate(unsorted):
        current = i
        while current > 0 and unsorted[current] < unsorted[current - 1]:
            # flip adjacent elements
            unsorted[current], unsorted[current - 1] = unsorted[current - 1], unsorted[current]
            current -= 1

            print(unsorted)

    return unsorted


def insertion_sort_2(unsorted: List[int]) -> List[int]:
    # iterate through the list / array
    for i in range(len(unsorted)):
        curr = i - 1
        # if current is greater than 0, compare the current and previous
        while 0 < curr <= i:
            if unsorted[curr] < unsorted[curr - 1]:
                unsorted[curr - 1], unsorted[curr] = unsorted[curr], unsorted[curr - 1]
                curr -= 1
            else:
                curr += 1

            print(unsorted)

    return unsorted


def insertion_sort_3(unsorted: List[int]) -> List[int]:
    for i in range(len(unsorted)):
        curr = i
        # while the current position is greater than the beginning of the list / array
        # compare the element at the current position and the prev position
        # if the element at the prev position is greater than the current position, flip them
        while curr > 0 and unsorted[curr] < unsorted[curr - 1]:
            unsorted[curr - 1], unsorted[curr] = unsorted[curr], unsorted[curr - 1]
            curr -= 1

            print("{} : {}".format(i, curr))
            print(unsorted)

    return unsorted


if __name__ == '__main__':
    print(insertion_sort([5, 3, 1, 2, 4]))
    print("")
    print(insertion_sort_2([5, 3, 1, 2, 4]))
    print("")
    print(insertion_sort_3([5, 3, 1, 2, 4]))
