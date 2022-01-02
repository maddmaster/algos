import sys
from typing import List


class Location:
    def __init__(self, x, y, distance=0):
        self.x = x
        self.y = y
        self.distance = distance

    def is_valid(self, size: int):
        if 0 <= self.x < size and 0 <= self.y < size:
            return True
        else:
            False

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __str__(self):
        return "Location(x={}, y={}, distance={})".format(self.x, self.y, self.distance)


possible_moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]


def find_shortest_distance(origin: Location, destination: Location, size):
    visited = set()

    to_visit: List[Location] = [origin]
    while to_visit:
        at = to_visit.pop(0)

        if at == destination:
            return at.distance

        if at not in visited:
            visited.add(at)

            for move in possible_moves:
                to = Location(at.x + move[0], at.y + move[1], at.distance + 1)
                if to.is_valid(size):
                    to_visit.append(to)

    return sys.maxsize


def main():
    print(find_shortest_distance(Location(0, 0), Location(7, 7), 8))


if __name__ == "__main__":
    main()
