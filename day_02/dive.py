import re


def solve(input_cmds):
    hor = dep =0
    for x in input_cmds:
        cmd = re.findall("(forward|up|down)", x)
        val = re.findall("[0-9]", x)
        if cmd[0] == 'forward':
            hor += int (val[0])
        elif cmd[0] == 'up':
            dep -= int (val[0])
        elif cmd[0] == 'down':
            dep += int(val[0])
    return hor * dep


def solve2(input_cmds):
    hor = dep = aim = 0
    for x in input_cmds:
        cmd = re.findall("(forward|up|down)", x)
        val = re.findall("[0-9]", x)
        if cmd[0] == 'forward':
            hor += int(val[0])
            dep += aim * int(val[0])
        elif cmd[0] == 'up':
            aim -= int(val[0])
        elif cmd[0] == 'down':
            aim += int(val[0])
    return hor * dep


with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    print('Solution part 1:')
    print(solve(lines))
    print('Solution part 2:')
    print(solve2(lines))
