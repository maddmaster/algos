from binarytree import build


def sample_tree_1():
    values = [7, 3, 2, 6, 9, None, 1, 5, 8]
    tree = build(values)
    return tree


def main():
    tree = sample_tree_1()
    print(tree)


if __name__ == "__main__":
    main()
