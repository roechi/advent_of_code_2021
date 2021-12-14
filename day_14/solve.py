from collections import Counter, defaultdict


def get_next_pairs(pair_map, letter_frequencies, rules):
    next_pair_map = defaultdict(int)

    for pair, frequency in pair_map.items():
        middle = rules[pair]
        next_pair_map[pair[0] + middle] += frequency
        next_pair_map[middle + pair[1]] += frequency
        letter_frequencies[middle] += frequency

    return next_pair_map


def solve(input_lines, iterations):
    template = input_lines[0].rstrip()

    rules = {}
    for line in input_lines[2:]:
        rule_segments = line.rstrip().split(' -> ')
        rules[rule_segments[0]] = rule_segments[1]

    pairs = Counter(a + b for a, b in zip(template, template[1:]))
    letter_frequencies = Counter(template)

    for i in range(iterations):
        pairs = get_next_pairs(pairs, letter_frequencies, rules)

    frequency_values = letter_frequencies.values()

    return max(frequency_values) - min(frequency_values)


with open('input.txt', 'r') as input_file:
    input_lines = input_file.readlines()

    print('Solution part 1:')
    print(solve(input_lines, 10))
    print('Solution part 2:')
    print(solve(input_lines, 40))
