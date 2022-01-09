from binarytree import build2

if __name__ == "__main__":
    input = [None if item == 'x' else int(item) for item in "6 4 3 x x 5 x x 8 x x".split()]
    tree = build2(input)
    print(tree)
