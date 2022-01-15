from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare the adjacent elements
        # the last element will always move immediately to the end hence the -i
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

            print(array)

    return array

def enhance_bubble_sort(array: List[int]) -> List[int]:
    # iterate thru each element
    for i in range(len(array)):

        is_sorted = True

        # loop thru to compare adjacent elements
        for j in range(0, len(array) -1 -i):
            # check adjacent elements and swap if necessary
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
                is_sorted = False

            print(array)

            if is_sorted:
                break

        return array


if __name__ == "__main__":
    print(bubble_sort([5, 3, 1, 2, 4]))
    print("")
    print(enhance_bubble_sort([5, 3, 1, 2, 4]))
    print("")
    print(enhance_bubble_sort([1, 2, 3, 4, 5]))
