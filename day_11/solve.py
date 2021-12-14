from queue import SimpleQueue

import numpy as np


def solve(input_lines):
    matr = [[int(i) for i in line.rstrip()] for line in input_lines]

    total_flashes = 0

    for step in range(100):
        for l in matr:
            print(l)
        print()
        flashes = SimpleQueue()

        for y in range(len(matr)):
            for x in range(len(matr[0])):
                matr[y][x] += 1
                if matr[y][x] > 9:
                    flashes.put((x, y))

        while flashes.qsize() > 0:
            flash_pos = flashes.get()
            if matr[flash_pos[1]][flash_pos[0]] > 9:
                total_flashes += 1
                matr[flash_pos[1]][flash_pos[0]] = 0
                for x, y in get_neighbours(flash_pos, matr):
                    if matr[y][x] != 0:
                        matr[y][x] += 1
                    if matr[y][x] > 9:
                        flashes.put((x, y))

    return total_flashes


def get_neighbours(point, matr):
    neighbours = []
    for vec in [
        np.array((1, 0)),
        np.array((-1, 0)),
        np.array((0, 1)),
        np.array((0, -1)),
        np.array((1, 1)),
        np.array((-1, 1)),
        np.array((1, -1)),
        np.array((-1, -1))
    ]:
        neighbor = np.array(point) + vec
        if 0 <= neighbor[0] < len(matr) and 0 <= neighbor[1] < len(matr[0]):
            neighbours.append((neighbor[0], neighbor[1]))

    return neighbours


def solve2(input_lines):
    matr = [[int(i) for i in line.rstrip()] for line in input_lines]

    total_flashes = 0

    synched = False
    step = 0

    while not synched:
        step += 1
        for l in matr:
            print(l)
        print()
        flashes = SimpleQueue()

        for y in range(len(matr)):
            for x in range(len(matr[0])):
                matr[y][x] += 1
                if matr[y][x] > 9:
                    flashes.put((x, y))

        while flashes.qsize() > 0:
            flash_pos = flashes.get()
            if matr[flash_pos[1]][flash_pos[0]] > 9:
                total_flashes += 1
                matr[flash_pos[1]][flash_pos[0]] = 0
                for x, y in get_neighbours(flash_pos, matr):
                    if matr[y][x] != 0:
                        matr[y][x] += 1
                    if matr[y][x] > 9:
                        flashes.put((x, y))

        if sum(sum(line) for line in matr) == 0:
            synched = True

    return step


with open('input.txt', 'r') as input_file:
    input_lines = input_file.readlines()

    print('Solution part 1:')
    print(solve(input_lines))
    print('Solution part 2:')
    print(solve2(input_lines))
