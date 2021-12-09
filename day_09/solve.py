import sys


def solve(lines):
    heatmap_matr = [[int(x) for x in line.rstrip()] for line in lines]

    heatmap = {}

    for y in range(len(heatmap_matr)):
        for x in range(len(heatmap_matr[0])):
            heatmap[(x, y)] = heatmap_matr[y][x]

    lows = []
    for point in heatmap.keys():
        x = point[0]
        y = point[1]

        up = heatmap[(x, y - 1)] if (x, y - 1) in heatmap else sys.maxsize
        down = heatmap[(x, y + 1)] if (x, y + 1) in heatmap else sys.maxsize
        left = heatmap[(x - 1, y)] if (x - 1, y) in heatmap else sys.maxsize
        right = heatmap[(x + 1, y)] if (x + 1, y) in heatmap else sys.maxsize

        if heatmap[point] < up and heatmap[point] < down and heatmap[point] < left and heatmap[point] < right:
            lows.append(heatmap[point])

    return sum(lows) + len(lows)


def find_adjacent_basin_points(points, heatmap):
    adjacent = set(points)
    for point in points:
        x = point[0]
        y = point[1]

        if (x, y - 1) in heatmap and heatmap[(x, y - 1)] < 9:
            adjacent.add((x, y - 1))
        if (x, y + 1) in heatmap and heatmap[(x, y + 1)] < 9:
            adjacent.add((x, y + 1))
        if (x - 1, y) in heatmap and heatmap[(x - 1, y)] < 9:
            adjacent.add((x - 1, y))
        if (x + 1, y) in heatmap and heatmap[(x + 1, y)] < 9:
            adjacent.add((x + 1, y))

    if not adjacent.issubset(set(points)):
        for p in adjacent:
            if p not in points:
                points.append(p)

        return find_adjacent_basin_points(points, heatmap)
    else:
        return points


def solve2(lines):
    heatmap_matr = [[int(x) for x in line.rstrip()] for line in lines]

    heatmap = {}

    for y in range(len(heatmap_matr)):
        for x in range(len(heatmap_matr[0])):
            heatmap[(x, y)] = heatmap_matr[y][x]

    basins = []
    for point in heatmap.keys():
        if heatmap[point] < 9:
            basin = set(find_adjacent_basin_points([point], heatmap))
            if basin not in basins:
                basins.append(basin)

    basins = sorted(basins, key=lambda x: len(x), reverse=True)

    return len(basins[0]) * len(basins[1]) * len(basins[2])


with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

    print('Solution part 1:')
    print(solve(lines))
    print('Solution part 2:')
    print(solve2(lines))
