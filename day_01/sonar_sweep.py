def sweep(raw_input: list[str]) -> int:
    measurements = list(map(int, raw_input))
    count = 0
    for i in range(len(measurements) - 1):
        if measurements[i + 1] > measurements[i]:
            count += 1

    return count


def sweep_window(raw_input: list[str], window_size: int) -> int:
    count = 0
    measurements = list(map(int, raw_input))
    for i in range(len(measurements) - window_size):
        if sum(measurements[i + 1:i + window_size + 1]) > sum(measurements[i:i + window_size]):
            count += 1

    return count


with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    print('Solution part 1:')
    print(sweep(lines))
    print('Solution part 2:')
    print(sweep_window(lines, 3))
