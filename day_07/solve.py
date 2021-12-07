def simple_dist(a, b):
    return abs(a - b)


def incremental_dist(a, b):
    return sum(range(1, abs(a - b) + 1))


def solve(input_line, dist_func):
    vec = [int(x) for x in input_line.rstrip().split(',')]
    dist = []
    for p in range(len(vec)):
        dists = [dist_func(p, x) for x in vec]
        dist.append(sum(dists))

    return min(dist)


with open('input.txt', 'r') as input_file:
    line = input_file.readline()

    print('Solution part 1:')
    print(solve(line, simple_dist))
    print('Solution part 2:')
    print(solve(line, incremental_dist))
