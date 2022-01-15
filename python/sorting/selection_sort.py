from typing import List


def selection_sort(unsorted: List[int]) -> List[int]:
    print(unsorted)
    # iterate through the list
    # this will track the sorted index
    for sorted_idx in range(len(unsorted)):
        min_idx = sorted_idx

        # iterate from i + 1, to end of list
        for unsorted_idx in range(sorted_idx + 1, len(unsorted)):
            print("{}, {}".format(unsorted[min_idx], unsorted[unsorted_idx]))
            if unsorted[unsorted_idx] < unsorted[min_idx]:
                min_idx = unsorted_idx

        # swap the value in the min_idx with the next sorted position
        unsorted[sorted_idx], unsorted[min_idx] = unsorted[min_idx], unsorted[sorted_idx]

        print(unsorted)

    return unsorted


if __name__ == "__main__":
    print(selection_sort([5, 3, 1, 2, 4]))
