import re

import numpy as np


def parse_line_pair(line_str):
    numbers = re.findall('([0-9]+)', line_str)
    numbers = list(map(int, numbers))

    return [np.array(numbers[:2]), np.array(numbers[2:])]


def is_horizontal_or_vertical(line_pair):
    return line_pair[0][0] == line_pair[1][0] or line_pair[0][1] == line_pair[1][1]


def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
       return v
    return v / norm


def solve(line_pairs):
    map = {}
    for raw_pair in line_pairs:
        pair = parse_line_pair(raw_pair)
        if is_horizontal_or_vertical(pair):

            if pair[0][0] == pair[1][0]:
                if pair[0][1] < pair[1][1]:
                    direction = np.array([0, 1])
                else:
                    direction = np.array([0, -1])
            else:
                if pair[0][0] < pair[1][0]:
                    direction = np.array([1, 0])
                else:
                    direction = np.array([-1, 0])

            curr_position = pair[0]
            while not np.array_equal(curr_position, pair[1]):
                if (curr_position[0], curr_position[1]) in map:
                    map[(curr_position[0], curr_position[1])] += 1
                else:
                    map[(curr_position[0], curr_position[1])] = 1
                curr_position = curr_position + direction

            if (curr_position[0], curr_position[1]) in map:
                map[(curr_position[0], curr_position[1])] += 1
            else:
                map[(curr_position[0], curr_position[1])] = 1

    vals = list(map.values())
    vals = list(filter(lambda x: x > 1, vals))
    return len(vals)


def solve2(line_pairs):
    map = {}
    for raw_pair in line_pairs:
        pair = parse_line_pair(raw_pair)
        if pair[0][0] == pair[1][0]:
            if pair[0][1] < pair[1][1]:
                direction = np.array([0, 1])
            else:
                direction = np.array([0, -1])
        elif pair[0][1] == pair[1][1]:
            if pair[0][0] < pair[1][0]:
                direction = np.array([1, 0])
            else:
                direction = np.array([-1, 0])
        else:
            if pair[0][0] < pair[1][0]:
                direction_x = 1
            else:
                direction_x = -1
            if pair[0][1] < pair[1][1]:
                direction_y = 1
            else:
                direction_y = -1
            direction = np.array([direction_x, direction_y])

        curr_position = pair[0]
        while not np.array_equal(curr_position, pair[1]):
            if (curr_position[0], curr_position[1]) in map:
                map[(curr_position[0], curr_position[1])] += 1
            else:
                map[(curr_position[0], curr_position[1])] = 1
            curr_position = curr_position + direction

        if (curr_position[0], curr_position[1]) in map:
            map[(curr_position[0], curr_position[1])] += 1
        else:
            map[(curr_position[0], curr_position[1])] = 1

    vals = list(map.values())
    vals = list(filter(lambda x: x > 1, vals))
    return len(vals)


with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    line_pairs = [parse_line_pair(l) for l in lines]

    print('Solution part 1:')
    print(solve(lines))
    print('Solution part 2:')
    print(solve2(lines))
