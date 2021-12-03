from functools import reduce

import numpy as np


def split(word):
    return [char for char in word]


def bin_array_to_int(bin_array):
    res = ''

    for i in bin_array:
        res += str(i)

    return int(res, 2)


def vectorize(lines):
    vecs = []
    for line in lines:
        l = split(line.rstrip())
        vecs.append(np.array(list(map(lambda x: int(x), l))))
    return vecs


def get_most_common_bit(vecs, pos):
    sum = reduce(lambda a, b: a + b, vecs)

    return 1 if sum[pos] >= len(vecs) / 2 else 0


def solve(lines):
    vecs = vectorize(lines)
    sum = reduce(lambda a, b: a + b, vecs)

    gamma = []
    epsilon = []
    for i in range(len(sum)):
        most_common = get_most_common_bit(vecs, i)
        gamma.append(most_common)
        epsilon.append((most_common + 1) % 2)

    return bin_array_to_int(gamma) * bin_array_to_int(epsilon)


def solve2(lines):
    vecs = vectorize(lines)

    oxygen = vecs
    i = 0
    while len(oxygen) > 1:
        filter_bit = get_most_common_bit(oxygen, i)
        oxygen = list(filter(lambda x: x[i] == filter_bit, oxygen))
        i += 1

    i = 0
    co2_scrubber = vecs
    while len(co2_scrubber) > 1:
        filter_bit = (get_most_common_bit(co2_scrubber, i) + 1) % 2
        co2_scrubber = list(filter(lambda x: x[i] == filter_bit, co2_scrubber))
        i += 1

    return bin_array_to_int(oxygen[0]) * bin_array_to_int(co2_scrubber[0])


with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    print('Solution part 1:')
    print(solve(lines))
    print('Solution part 2:')
    print(solve2(lines))
