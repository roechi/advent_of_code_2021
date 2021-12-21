import numpy as np


def solve(input_lines):
    split = input_lines[0].rstrip().split(' ')
    x_area = split[2][2:-1].split('..')
    y_area = split[3][2:].split('..')
    x_area = [int(x) for x in x_area]
    y_area = [int(y) for y in y_area]

    max_height = 0
    hitting_vels = set()
    for x in range(max(x_area) + 1):
        for y in range(min(y_area), abs(min(y_area)) + 1):
            pos = np.array([0, 0])
            vel = np.array([x, y])
            max_height_try = 0
            while not has_missed(pos, max(x_area), min(y_area)):
                pos += vel
                max_height_try = max(max_height_try, pos[1])
                if has_hit(pos, x_area, y_area):
                    max_height = max(max_height, max_height_try)
                    hitting_vels.add((x, y))
                if vel[0] > 0:
                    vel += np.array([-1, 0])
                elif vel[0] < 0:
                    vel += np.array([1, 0])
                vel += np.array([0, -1])

    return max_height, len(hitting_vels)


def has_hit(pos, x_area, y_area):
    return x_area[0] <= pos[0] <= x_area[1] and y_area[0] <= pos[1] <= y_area[1]


def has_missed(pos, x_max, y_min):
    return pos[0] > x_max or pos[1] < y_min


with open('input.txt', 'r') as input_file:
    input_lines = input_file.readlines()

    sol1, sol2 = solve(input_lines)
    print('Solution part 1:')
    print(sol1)
    print('Solution part 2:')
    print(sol2)
