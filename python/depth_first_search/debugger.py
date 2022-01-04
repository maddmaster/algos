from binarytree import build

if __name__ == "__main__":
    input = [None if item == 'x' else int(item) for item in "1 2 4 x 7 x x 5 x x 3 x 6 8 x x x".split()]
    tree = build(input)
    print(tree)




        7
    2
        x


1


        x
    4
        x