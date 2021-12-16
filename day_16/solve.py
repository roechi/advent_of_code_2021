from functools import reduce


def solve(input_lines):
    bin_str = ''

    for c in input_lines[0].rstrip():
        b = bin(int(c, 16))[2:].zfill(4)
        bin_str += str(b)

    versions = []
    sub_packet_vals = []
    parse(bin_str, versions, sub_packet_vals)
    return sum(versions)


def parse(bin_str, versions, sub_packet_vals):
    version = int(bin_str[:3], 2)
    versions.append(version)
    type = int(bin_str[3:6], 2)
    pos = 6
    if type == 4:
        return read_literal(bin_str[pos:], sub_packet_vals) + pos
    else:
        length_type = int(bin_str[pos])
        pos += 1
        internal_sub_packet_vals = []
        if length_type == 0:
            length = int(bin_str[pos:pos + 15], 2)
            pos += 15
            parsed_bits = 0
            while parsed_bits != length:
                parsed_bits += parse(bin_str[pos + parsed_bits:pos + length], versions, internal_sub_packet_vals)
            pos += length
        elif length_type == 1:
            number_of_subpackets = int(bin_str[pos:pos + 11], 2)
            pos += 11
            parsed_packets = 0
            parsed_bits = 0
            while parsed_packets != number_of_subpackets:
                parsed_bits += parse(bin_str[pos + parsed_bits:], versions, internal_sub_packet_vals)
                parsed_packets += 1
            pos += parsed_bits

        if type == 0:
            sub_packet_vals.append(sum(internal_sub_packet_vals))
        elif type == 1:
            sub_packet_vals.append(reduce(lambda a,b: a * b, internal_sub_packet_vals))
        elif type == 2:
            sub_packet_vals.append(min(internal_sub_packet_vals))
        elif type == 3:
            sub_packet_vals.append(max(internal_sub_packet_vals))
        elif type == 5:
            sub_packet_vals.append(1 if internal_sub_packet_vals[0] > internal_sub_packet_vals[1] else 0)
        elif type == 6:
            sub_packet_vals.append(1 if internal_sub_packet_vals[0] < internal_sub_packet_vals[1] else 0)
        elif type == 7:
            sub_packet_vals.append(1 if internal_sub_packet_vals[0] == internal_sub_packet_vals[1] else 0)
    return pos


def read_literal(bin_str, sub_packet_vals):
    int_pos = 0
    last_group = False
    groups = ''
    while not last_group:
        if bin_str[int_pos] == '0':
            last_group = True
        groups += bin_str[int_pos + 1: int_pos + 5]
        int_pos += 5

    sub_packet_vals.append(int(groups, 2))
    return int_pos


def solve2(input_lines):
    bin_str = ''

    for c in input_lines[0].rstrip():
        b = bin(int(c, 16))[2:].zfill(4)
        bin_str += str(b)

    versions = []
    sub_packet_vals = []
    parse(bin_str, versions, sub_packet_vals)
    return sub_packet_vals[0]


with open('input.txt', 'r') as input_file:
    input_lines = input_file.readlines()

    print('Solution part 1:')
    print(solve(input_lines))
    print('Solution part 2:')
    print(solve2(input_lines))
