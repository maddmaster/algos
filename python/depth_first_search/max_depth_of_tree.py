class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_max_depth(root: Node) -> int:
    def dfs(root: Node):
        if not root:
            return 0

        # height of left subtree or height of right subtree whichever is bigger + 1 (for the root)
        return max(dfs(root.left), dfs(root.right)) + 1

    return dfs(root)


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    root = build_tree(iter("5 4 3 x x 8 x x 6 x x".split()), int)
    res = tree_max_depth(root)
    print(res)
