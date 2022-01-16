def partition(array, low, high):
    print(" partition -> {}, low -> {}, right -> {}".format(array, low, high))
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

        print("   compare -> {}, j -> {}, i -> {}, pivot -> {}".format(array, j, i, pivot))

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    print("   compare -> {}, j -> {}, i -> {}, pivot -> {}".format(array, j, i, pivot))

    # return the position from where partition is done
    return i + 1


# function to perform quicksort
def quick_sort(array, left, right):
    print("quick sort -> {}".format(array))
    if left < right:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        ptn_idx = partition(array, left, right)

        print(" partitioned at index -> {}".format(ptn_idx))

        # recursive call on the left of pivot
        quick_sort(array, left, ptn_idx - 1)

        # recursive call on the right of pivot
        quick_sort(array, ptn_idx + 1, right)


if __name__ == "__main__":
    array = [8, 7, 2, 1, 0, 9, 6]
    quick_sort(array, 0, len(array) - 1)
    print("sorted -> {}".format(array))
