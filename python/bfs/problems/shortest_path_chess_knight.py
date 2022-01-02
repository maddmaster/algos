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
        return (self.x, self.y, self.distance) == (other.x, other.y, other.distance)

    def __str__(self):
        return "Location(x={}, y={})".format(self.x, self.y, self.distance)


possible_moves = [(2, -1), (2, 1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


def find_shortest_distance(origin: Location, destination: Location, size):
    visited = set()

    to_visit: List[Location] = [origin]

    while to_visit:
        location = to_visit.pop()

        if location.x == destination.x and location.y == destination.y:
            return location.distance

        if location not in visited:
            visited.add(location)

            for move in possible_moves:
                to = Location(location.x + move[0], location.y + move[1], location.distance + 1)
                print("to: {}".format(to))
                if to.is_valid(size):
                    to_visit.append(to)

    return sys.maxsize

def main():
    print(find_shortest_distance(Location(0, 0), Location(7, 7), 8))

    """
    origin = Location(0, 0)
    print(origin)
    destination = Location(1, 2)
    print(destination)
    at = Location(1, 2)
    print(at)
    print(destination == at)
    print(destination == origin)

    foo = Location(0, 0, 1)
    visited = [origin]
    print(visited)
    print(foo in visited)
    """



if __name__ == "__main__":
    main()
