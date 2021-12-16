from functools import reduce

class Reader:
    txt: str
    ptr: int

    def __init__(self, txt):
        self.txt = txt
        self.ptr = 0

    def next(self, n=1):
        res = []
        for _ in range(n):
            res.append(self.txt[self.ptr])
            self.ptr += 1
        return ''.join(res)

def get_bin_str(hex_str: str):
    hx = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    return ''.join([hx[c] for c in hex_str])

def read_file(file_path: str):
    hex_str = ''.join([s.strip() for s in open(file_path).readlines()])
    return get_bin_str(hex_str)

def parse_literal(reader: Reader) -> int:
    value_bin = []

    while True:
        five_seq = reader.next(5)
        value_bin.append(five_seq[1:])

        if five_seq[0] == '0':
            break

    literal_value = int(''.join(value_bin), base=2)

    return literal_value

def parse_op(reader: Reader) -> list[int]:
    answers = []

    len_type_id = reader.next()

    if len_type_id == '0':

        subpackets_len = int(reader.next(15), base=2)

        termination_bit = reader.ptr + subpackets_len

        while reader.ptr < termination_bit:
            answers.append(parse_packet(reader))

    elif len_type_id == '1':

        num_subpackets = int(reader.next(11), base=2)

        for _ in range(num_subpackets):
            answers.append(parse_packet(reader))

    return answers

def parse_packet(reader: Reader) -> int:
    version = int(reader.next(3), base=2)
    pack_type = int(reader.next(3), base=2)

    match pack_type:
        # sum
        case 0:
            return sum(parse_op(reader))
        # product
        case 1:
            return reduce(lambda x, y: x*y, parse_op(reader))
        # min
        case 2:
            return min(parse_op(reader))
        # max
        case 3:
            return max(parse_op(reader))
        # literal
        case 4:
            return parse_literal(reader)
        # greater than
        case 5:
            first, second = parse_op(reader)
            return 1 if first > second else 0
        # less than
        case 6:
            first, second = parse_op(reader)
            return 1 if first < second else 0
        # equal to
        case 7:
            first, second = parse_op(reader)
            return 1 if first == second else 0

if __name__ == "__main__":
    # parse input
    binstr = read_file('input.txt')
    # binstr = get_bin_str('9C0141080250320F1802104A08')
    # binstr = '11101110000000001101010000001100100000100011000001100000'

    reader = Reader(binstr)

    ans = parse_packet(reader)
    print(ans)
