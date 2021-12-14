import re

import numpy as np

def print_points(points):
    x_max = max([t[0] for t in points])
    y_max = max([t[1] for t in points])

    matr = [['.' for x in range(x_max + 1)] for y in range(y_max + 1)]

    for point in points:
        matr[point[1]][point[0]] = '#'

    for line in matr:
        print(line)
    print()


def solve(input_lines):
    coords = []
    fold_instructions = []

    for line in input_lines:
        if re.match('[0-9]+,[0-9]+', line.rstrip()):
            coords.append(line.rstrip())
        elif re.match('^fold', line.rstrip()):
            fold_instructions.append(line.rstrip().split()[2])

    points = []

    for line in coords:
        split = line.split(',')
        points.append(np.array((int(split[0]), int(split[1]))))



    for fold in fold_instructions:

        folded_points = []
        axis = int(fold.split('=')[1])
        if fold[0] == 'x':
            for point in points:
                if axis < point[0]:
                    dist = abs(axis - point[0])
                    folded_points.append(point - np.array((2 * dist, 0)))
                else:
                    folded_points.append(point)

        elif fold[0] == 'y':
            for point in points:
                if axis < point[1]:
                    dist = abs(axis - point[1])
                    folded_points.append(point - np.array((0, 2 * dist)))
                else:
                    folded_points.append(point)
        points = folded_points

    reduced = set()
    for point in points:
        reduced.add((point[0], point[1]))

    print_points(reduced)



    return len(reduced)


def solve2(input_lines):
    pass



with open('input.txt', 'r') as input_file:
    input_lines = input_file.readlines()

    print('Solution part 1:')
    print(solve(input_lines))
    print('Solution part 2:')
    print(solve2(input_lines))
