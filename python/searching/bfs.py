from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return "Node(data: {}, left: {}, right:{})".format(self.data, self.left, self.right)


class Solution:
    def build_tree(self, in_order, pre_order):

        if len(in_order) == 0:
            return None

        if len(in_order) == 1:
            return Node(in_order[0])

        data = pre_order[0]
        root = Node(data)

        index = in_order.index(data)

        left_in_order = in_order[:index]
        right_in_order = in_order[index + 1:]
        print("{}, {}, {}".format(left_in_order, root.data, right_in_order))

        left_pre_order = pre_order[1: len(left_in_order) + 1]
        right_pre_order = pre_order[1 + len(left_pre_order):]
        print("{}, {}, {}".format(left_pre_order, root.data, right_pre_order))

        root.left = self.build_tree(left_in_order, left_pre_order)
        root.right = self.build_tree(right_in_order, right_pre_order)

        return root


def main():
    solution = Solution()

    in_order = list("DBEAFC")
    pre_order = list("ABDECF")

    root = solution.build_tree(in_order, pre_order)
    print(root)


if __name__ == '__main__':
    main()
