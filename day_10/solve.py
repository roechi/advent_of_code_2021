pairs = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>'
    }


def find_first_illegal(line):
    stack = []
    for c in line.rstrip():
        if c in pairs.keys():
            stack.append(c)
        else:
            if c == pairs[stack[-1]]:
                stack.pop()
            else:
                return c
    if len(stack) > 0 and stack[-1] in pairs.values():
        return stack[-1]
    else:
        return None


def solve(lines):
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    scoring = []
    for line in lines:
        illegal = find_first_illegal(line)
        if illegal:
            scoring.append(scores[illegal])
    return sum(scoring)


def find_middle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return input_list[int(middle)], input_list[int(middle - 1)]


def find_completion_sequence(line):

    c_to_complete = []
    stack = []
    for c in list(line.rstrip()).__reversed__():
        if c in pairs.keys():
            if len(stack) > 0 and pairs[c] == stack[-1]:
                stack.pop()
            else:
                c_to_complete.append(pairs[c])
        else:
            stack.append(c)
    return c_to_complete


def solve2(lines):
    scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    completions = []
    for line in lines:
        if not find_first_illegal(line):
            completions.append(find_completion_sequence(line))

    scoring = []
    for completion in completions:
        s = 0
        for c in completion:
            s *= 5
            s += scores[c]
        scoring.append(s)

    scoring.sort()

    return find_middle(scoring)


with open('input.txt', 'r') as input_file:
    input_lines = input_file.readlines()

    print('Solution part 1:')
    print(solve(input_lines))
    print('Solution part 2:')
    print(solve2(input_lines))
