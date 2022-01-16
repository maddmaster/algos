from typing import List


# python is pass by reference
def merge_sort(array: List[int]):
    print("input: {}".format(array))

    if len(array) > 1:

        mid = len(array) // 2

        left = array[:mid]
        right = array[mid:]

        print("left: {}".format(left))
        print("right: {}".format(right))

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

        print("sorted: {}".format(array))


if __name__ == "__main__":
    array: List[int] = [5, 3, 1, 2, 4]
    merge_sort(array)
    print(array)
