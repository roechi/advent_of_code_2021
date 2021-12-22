import collections
import re


def solve(input_lines):
    cubes = collections.defaultdict(int)

    for toggle, new_cube in map(str.split, input_lines):
        cube_raw = tuple([int(val) for val in re.findall(r'-?\d+', new_cube)])

        intersection = get_intersection(cube_raw, (-50, 50, -50, 50, -50, 50))
        if intersection:
            new_cube = intersection

            for existing_cube, state in cubes.copy().items():
                intersection = get_intersection(new_cube, existing_cube)
                if intersection:
                    cubes[intersection] -= state

            if toggle == 'on':
                cubes[new_cube] += 1

    return sum(calc_cube_val(cube, val) for cube, val in cubes.items())


def solve2(input_lines):
    cubes = collections.defaultdict(int)
    for toggle, new_cube in map(str.split, input_lines):
        new_cube = tuple([int(val) for val in re.findall(r'-?\d+', new_cube)])

        for existing_cube, state in cubes.copy().items():
            intersection = get_intersection(new_cube, existing_cube)
            if intersection:
                cubes[intersection] -= state

        if toggle == 'on':
            cubes[new_cube] += 1

    return sum(calc_cube_val(c, v) for c, v in cubes.items())


def cut_region(min_v, max_v, val):
    val = max(min_v, val)
    val = min(max_v, val)
    return val


def get_intersection(first_cube, second_cube):
    x = max(first_cube[0], second_cube[0])
    y = max(first_cube[2], second_cube[2])
    z = max(first_cube[4], second_cube[4])
    X = min(first_cube[1], second_cube[1])
    Y = min(first_cube[3], second_cube[3])
    Z = min(first_cube[5], second_cube[5])

    if x <= X and y <= Y and z <= Z:
        return x, X, y, Y, z, Z
    else:
        return None


def calc_cube_val(cube, val):
    return (abs(cube[1] - cube[0]) + 1) * (abs(cube[3] - cube[2]) + 1) * (abs(cube[5] - cube[4]) + 1) * val


with open('input.txt', 'r') as input_file:
    input_lines = input_file.readlines()

    print('Solution part 1:')
    print(solve(input_lines))
    print('Solution part 2:')
    print(solve2(input_lines))
