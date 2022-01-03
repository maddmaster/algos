import base2
from binarytree import Node

# used for shortest path
def traverse_breadth_first_iterative(root):

    if root is None:
        return

    queue = [root]

    while len(queue) > 0:
        node = queue.pop(0)
        print(node.value)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


def main():
    tree = base2.sample_tree_1()
    print(tree)
    traverse_breadth_first_iterative(tree)


if __name__ == "__main__":
    main()
