from trees import Node, build_tree


def get_height(tree: Node) -> int:
    if not tree:
        return 0

    left_subtree_height = get_height(tree.left)  # height of left subtree
    right_subtree_height = get_height(tree.right)  # height of right subtree

    # the height of the tree would be the max between left subtree and right subtree + 1
    return max(left_subtree_height, right_subtree_height) + 1


def is_balanced_wrong(tree: Node) -> bool:

    left_subtree_height = get_height(tree.left)
    right_subtree_height = get_height(tree.right)

    if abs(left_subtree_height - right_subtree_height) > 1:
        return False
    else:
        return True


def is_balanced(tree: Node) -> bool:
    # an empty tree is balanced
    if not tree:
        return True

    left_subtree_height = get_height(tree.left)
    right_subtree_height = get_height(tree.right)

    # if the diff in height for subtrees is <= 1 and left subtree and right subtree are balanced then tree is
    # balanced...
    if not is_balanced(tree.left) or not is_balanced(tree.right) or abs(left_subtree_height - right_subtree_height) > 1:
        return False
    else:
        return True



if __name__ == '__main__':
    tree = build_tree(iter("1 2 4 x 7 x x 5 x x 3 x 6 8 x x x".split()), int)
    res = is_balanced(tree)
    print('true' if res else 'false')




