def solve(input_lines, passes):
    enhancement_algo = input_lines[0].rstrip()
    raw_image = [line.rstrip() for line in input_lines[2:]]

    image_dict = {}

    for y in range(len(raw_image)):
        for x in range(len(raw_image[0])):
            image_dict[(x, y)] = 1 if raw_image[y][x] == '#' else 0
    void_flip = 0
    for i in range(passes):
        image_dict_copy = image_dict.copy()
        sorted_points = sorted(image_dict.keys(), key=lambda x: x[0] + x[1])
        upper_left = (sorted_points[0][0] - 2, sorted_points[0][1] - 2)
        lower_right = (sorted_points[-1][0] + 2, sorted_points[-1][1] + 2)

        for y in range(upper_left[1], lower_right[1] + 1):
            for x in range(upper_left[0], lower_right[0] + 1):
                target_idx = evaluate_region((x, y), image_dict, void_flip)

                if enhancement_algo[target_idx] == '#':
                    image_dict_copy[(x, y)] = 1
                else:
                    image_dict_copy[(x, y)] = 0
        image_dict = image_dict_copy
        void_flip += 1
        void_flip %= 2

    return sum(image_dict.values())


def evaluate_region(middle, image_dict, void_flip):
    min_x = middle[0] - 1
    min_y = middle[1] - 1
    max_x = middle[0] + 1
    max_y = middle[1] + 1

    bin_str = ''
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in image_dict.keys():
                bin_str += str(image_dict[(x, y)])
            else:
                bin_str += str(void_flip)

    return int(bin_str, 2)


with open('input.txt', 'r') as input_file:
    input_lines = input_file.readlines()

    print('Solution part 1:')
    print(solve(input_lines, 2))
    print('Solution part 2:')
    print(solve(input_lines, 50))
