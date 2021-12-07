

def simulate(fish_init_state, days):
    timers = [0] * 9

    for i in fish_init_state:
        timers[i] += 1

    for i in range(days):
        at_zero = timers[0]

        for a in range(1, len(timers)):
            timers[a - 1] = timers[a]

        timers[6] += at_zero
        timers[8] = at_zero
    return sum(timers)


with open('input.txt', 'r') as input_file:
    line = input_file.readline()
    init_state = [int(f) for f in line.rstrip().split(',')]

    print('Solution part 1:')
    print(simulate(init_state, 80))
    print('Solution part 2:')
    print(simulate(init_state, 256))
