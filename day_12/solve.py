import re
from collections import Counter


def solve(input_lines):
    graph = {}
    for line in input_lines:
        nodes = re.findall('([a-zA-Z]+)', line.rstrip())
        if not nodes[0] in graph:
            graph[nodes[0]] = [nodes[1]]
        else:
            graph[nodes[0]] += [nodes[1]]
        if not nodes[1] in graph:
            graph[nodes[1]] = [nodes[0]]
        else:
            graph[nodes[1]] += [nodes[0]]

    paths = []
    current = ['start']
    find_paths_one(graph, current, paths)
    for path in paths:
        print(path)
    return len(paths)


def find_paths_one(graph: dict, current_path: list, found_paths: list):
    if current_path[-1] not in graph.keys():
        return
    children = graph[current_path[-1]]
    for c in children:
        branching_path = current_path.copy()
        if c == 'end':
            found = branching_path.copy()
            found.append(c)
            found_paths.append(found)
        elif str(c).islower():
            if c not in current_path:
                branching_path.append(c)
                find_paths_one(graph, branching_path, found_paths)
        else:
            branching_path.append(c)
            find_paths_one(graph, branching_path, found_paths)


def solve2(input_lines):
    graph = {}
    for line in input_lines:
        nodes = re.findall('([a-zA-Z]+)', line.rstrip())
        if not nodes[0] in graph:
            graph[nodes[0]] = [nodes[1]]
        else:
            graph[nodes[0]] += [nodes[1]]
        if not nodes[1] in graph:
            graph[nodes[1]] = [nodes[0]]
        else:
            graph[nodes[1]] += [nodes[0]]

    paths = []
    current = ['start']
    find_paths_two(graph, current, paths)
    for path in paths:
        print(path)
    return len(paths)


def find_paths_two(graph: dict, current_path: list, found_paths: list):
    if current_path[-1] not in graph.keys():
        return
    children = graph[current_path[-1]]
    for c in children:
        branching_path = current_path.copy()
        if c == 'end':
            found = branching_path.copy()
            found.append(c)
            found_paths.append(found)
        elif str(c).islower():
            if c != 'start':
                if c not in current_path or not contains_double_lower(current_path):
                    branching_path.append(c)
                    find_paths_two(graph, branching_path, found_paths)

        else:
            branching_path.append(c)
            find_paths_two(graph, branching_path, found_paths)


def contains_double_lower(path):
    lowers = list(filter(lambda x: x.islower(), path))
    cave_frequencies = Counter(lowers)
    return max(cave_frequencies.values()) > 1


with open('input.txt', 'r') as input_file:
    input_lines = input_file.readlines()

    print('Solution part 1:')
    print(solve(input_lines))
    print('Solution part 2:')
    print(solve2(input_lines))
