

def solve(lines):
    outputs = [line.split('|')[1].lstrip().rstrip().split(' ') for line in lines]
    unique_outs = []
    for i in outputs:
        unique_outs.extend(list(filter(lambda x: len(x) in [2, 4, 3, 7], i)))
    return len(unique_outs)


def get_by_length(vals, length):
    return list(filter(lambda x: len(x) == length, vals))


def contains(a, b):
    mask = [x in b for x in a]
    return len(list(filter(lambda x: x == True, mask))) == len(a)


def solve2(lines):
    inputs = [line.split('|')[0].lstrip().rstrip().split(' ') for line in lines]
    outputs = [line.split('|')[1].lstrip().rstrip().split(' ') for line in lines]
    vals = []
    for i in range(len(inputs)):
        input = inputs[i]
        output = outputs[i]

        one = get_by_length(input, 2)[0]
        four = get_by_length(input, 4)[0]
        seven = get_by_length(input, 3)[0]
        eight = get_by_length(input, 7)[0]

        six_and_nine_and_zero = get_by_length(input, 6)
        nine_and_zero = list(filter(lambda x: contains(one, x) , six_and_nine_and_zero))
        nine = list(filter(lambda x: contains(four, x), nine_and_zero))[0]
        zero = list(filter(lambda x: x != nine, nine_and_zero))[0]
        six = list(filter(lambda x: x != nine and x != zero, six_and_nine_and_zero))[0]

        two_and_three_and_five = get_by_length(input, 5)

        five = list(filter(lambda x: contains(x, six), two_and_three_and_five))[0]

        two_and_three = list(filter(lambda x: x != five, two_and_three_and_five))
        three = list(filter(lambda x: contains(one, x), two_and_three))[0]
        two = list(filter(lambda x: x != three, two_and_three))[0]

        digits = {
            str(sorted(zero)): 0,
            str(sorted(one)): 1,
            str(sorted(two)): 2,
            str(sorted(three)): 3,
            str(sorted(four)): 4,
            str(sorted(five)): 5,
            str(sorted(six)): 6,
            str(sorted(seven)): 7,
            str(sorted(eight)): 8,
            str(sorted(nine)): 9
        }

        output = 1000 * digits[str(sorted(output[0]))] + 100 * digits[str(sorted(output[1]))] + 10 * digits[str(sorted(output[2]))] + digits[str(sorted(output[3]))]
        vals.append(output)

    return sum(vals)


with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

    print('Solution part 1:')
    print(solve(lines))
    print('Solution part 2:')
    print(solve2(lines))
