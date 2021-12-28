from typing import List


def linear_search(items: List[str], search_for: str) -> int:
    for i, item in enumerate(items):
        if item == search_for:
            return i

    return - 1


def main():
    str = "ABCD"
    print("position: {}".format(linear_search(list(str), "C")))


if __name__ == '__main__':
    main()
