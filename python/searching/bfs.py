from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return "Mode(data: {}, left: {}, right:{})".format(self.data, self.left, self.right)


def build_tree(in_order: List[str], pre_order: List[str], in_start: int, in_end: str, pre_index: int):
    if in_start > in_end:
        return None
    else:
        node = Node(pre_order[pre_index])
        pre_index += 1

        if in_start == in_end:
            return node
        else:
            in_index = search(in_order, in_start, in_end, node.data)

            node.left = build_tree(in_order, pre_order, in_start, in_index - 1, pre_index)
            node.right = build_tree(in_order, pre_order, in_index + 1, in_end, pre_index)

        return node


def search(in_order, start, end, value):
    for i in range(start, end + 1):
        if in_order[i] == value:
            return i


def main():
    in_order = list("DBEAFC")
    pre_order = list("ABDECF")

    root = build_tree(in_order, pre_order, 0, len(in_order) - 1, 0)


if __name__ == '__main__':
    main()
