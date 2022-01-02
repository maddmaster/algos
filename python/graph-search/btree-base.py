from graphviz import Digraph


class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

    def __str__(self):
        return "Node(data: {}, left: {}, right:{})".format(self.value, self.left, self.right)


class Solution:
    def build_tree(self, in_order, pre_order):

        # serves as stop conditions during recursion
        if len(in_order) == 0:
            return None

        if len(in_order) == 1:
            return Node(in_order[0])

        data = pre_order[0]
        root = Node(data)

        index = in_order.index(data)

        # divide the inorder tree to smaller problems (i.e. left and right subtree)
        left_in_order = in_order[:index]
        right_in_order = in_order[index + 1:]
        print("{}, {}, {}".format(left_in_order, root.value, right_in_order))

        # divide the preorder tree to smaller problems (i.e left and right preorder)
        left_pre_order = pre_order[1: len(left_in_order) + 1]
        right_pre_order = pre_order[1 + len(left_pre_order):]
        print("{}, {}, {}".format(left_pre_order, root.value, right_pre_order))

        # solve the sub problems
        root.left = self.build_tree(left_in_order, left_pre_order)
        root.right = self.build_tree(right_in_order, right_pre_order)

        return root


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.value)
        print_tree(node.right, level + 1)


def visualize_using_graphviz(root: Node):
    def add_nodes_and_edges(root: Node, dot=None):
        if dot is None:
            dot = Digraph()
            dot.node(name=root.value, label=root.value)

        if root.left:
            dot.node(name=root.left.value, label=root.left.value)
            dot.edge(root.value, root.left.value)
            dot = add_nodes_and_edges(root.left, dot=dot)

        if root.right:
            dot.node(name=root.right.value, label=root.right.value)
            dot.edge(root.value, root.right.value)
            dot = add_nodes_and_edges(root.right, dot=dot)

        return dot

    dot = add_nodes_and_edges(root)

    return dot


def main():
    solution = Solution()

    in_order = list("DBEAFC")
    pre_order = list("ABDECF")

    root = solution.build_tree(in_order, pre_order)
    print_tree(root)

    dot = visualize_using_graphviz(root)
    print(dot)
    dot.render(view=True)



if __name__ == '__main__':
    main()
