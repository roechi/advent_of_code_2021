import heapq
import sys
from collections import defaultdict

import numpy as np


def solve(input_lines):
    grid = [[int(x) for x in line.rstrip()] for line in input_lines]

    return shortest_path(grid, 1)


def solve2(input_lines):
    grid = [[int(x) for x in line.rstrip()] for line in input_lines]

    return shortest_path(grid, 5)


def get_valid_neighbours(pos, grid, current_path, size):
    next = []
    for vec in [
        np.array((1, 0)),
        np.array((0, 1)),
        np.array((-1, 0)),
        np.array((0, -1))
    ]:
        moved_pos = tuple(vec + np.array(pos))
        if 0 <= moved_pos[0] < len(grid) * size and 0 <= moved_pos[1] < len(grid[0]) * size:
            if moved_pos not in current_path:
                next.append(moved_pos)

    return next

def shortest_path(grid, size):
    dimension = len(grid)
    values = defaultdict(lambda: sys.maxsize)
    values[(0, 0)] = 0

    queue = []
    heapq.heappush(queue, (0, (0, 0)))

    visited = set()

    while queue:
        current_value, current = heapq.heappop(queue)

        if current in visited:
            continue

        for neighbour in get_valid_neighbours(current, grid, visited, size):
            cost = values[neighbour]
            neighbour_risk = get_risk(grid, size, neighbour)

            if cost > current_value + neighbour_risk:
                cost = current_value + neighbour_risk
                values[neighbour] = cost
                heapq.heappush(queue, (cost, neighbour))

    return values[size * dimension - 1, size * dimension - 1]


def get_risk(grid, size, point):
    dimension = len(grid)

    if not 0 <= point[0] < dimension * size:
        return sys.maxsize
    if not 0 <= point[1] < dimension * size:
        return sys.maxsize

    risk = point[0] // dimension + point[1] // dimension + grid[(point[0] % dimension)][(point[1] % dimension)]

    return 1 + risk % 10 if risk > 9 else risk


with open('input.txt', 'r') as input_file:
    input_lines = input_file.readlines()

    print('Solution part 1:')
    print(solve(input_lines))
    print('Solution part 2:')
    print(solve2(input_lines))
