from trees import Node


def lca(root: Node, node1: Node, node2: Node) -> Node:
    # empty tree
    if not root:
        return

    # if one of the target node is the root, then the LCA is the root
    if node1 == root or node2 == root:
        return root

    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    # case 1
    if left and right:
        return root


if __name__ == "__main__":
    # driver code, do not modify
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur


    def find_node(root, target):
        if not root: return
        if root.val == target: return root
        return find_node(root.left, target) or find_node(root.right, target)


    s = "6 4 3 x x 5 x x 8 x x".split()
    root = build_tree(iter(s))
    node1 = find_node(root, 4)
    node2 = find_node(root, 8)
    ans = lca(root, node1, node2)
    if not ans:
        print('null')
    else:
        print(ans.val)
