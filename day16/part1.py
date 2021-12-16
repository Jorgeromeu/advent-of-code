class Reader:
    txt: str
    ptr: int
    version_sum: int

    def __init__(self, txt):
        self.txt = txt
        self.ptr = 0
        self.version_sum = 0

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
        five_seq = reader.next(n=5)
        value_bin.append(five_seq[1:])

        if five_seq[0] == '0':
            break

    literal_value = int(''.join(value_bin), base=2)

    return literal_value

def parse_op(reader: Reader):
    len_type_id = reader.next()

    if len_type_id == '0':

        subpackets_len = int(reader.next(n=15), base=2)

        termination_bit = reader.ptr + subpackets_len

        i = 0
        while reader.ptr < termination_bit:
            parse_packet(reader)
            i += 1

    elif len_type_id == '1':

        num_subpackets = int(reader.next(n=11), base=2)

        for _ in range(num_subpackets):
            parse_packet(reader)

def parse_packet(reader: Reader):
    version = reader.next(n=3)
    pack_type = reader.next(n=3)

    # update version-sum
    reader.version_sum += int(version, base=2)

    # literal packet
    if int(pack_type, base=2) == 4:
        val = parse_literal(reader)

    # operator packet
    else:
        parse_op(reader)

if __name__ == "__main__":
    # parse input
    binstr = read_file('input.txt')
    # binstr = get_bin_str('620080001611562C8802118E34')
    # binstr = '11101110000000001101010000001100100000100011000001100000'

    reader = Reader(binstr)

    parse_packet(reader)

    print('sum', reader.version_sum)
