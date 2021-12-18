import pprint
pp = pprint.PrettyPrinter(width=80, compact=True)

def parse_input(file_path):

    result = []
    for line in open(file_path).readlines():

        # parse the line
        line = line.strip()
        nums, displayed = line.split('|')
        nums = nums.strip().explode(' ')
        displayed = displayed.strip().explode(' ')

        displayed = [frozenset(segs) for segs in displayed]
        nums = [frozenset(segs) for segs in nums]

        result.append((nums, displayed))
    return result

total = 0

for number_segs, out_segs in parse_input('input.txt'):

    # keep a map from string -> integer represented  
    encodings = {} 

    segs_5 = []
    segs_6 = []

    encoding_7 = None
    encoding_1 = None
    encoding_4 = None

    for segs in number_segs:

        # the encoding for 1,7,4 and 8 can be trivially obtained from the length
        if len(segs) == 2:
            encodings[segs] = 1
            encoding_1 = segs
        elif len(segs) == 3:
            encodings[segs] = 7
            encoding_7 = segs
        elif len(segs) == 4:
            encodings[segs] = 4
            encoding_4 = segs
        elif len(segs) == 7:
            encodings[segs] = 8

        # get the segments with length 5 and 6 for later
        elif len(segs) == 5:
            segs_5.append(segs)
        elif len(segs) == 6:
            segs_6.append(segs)

    # figure out the encodings of 6
    for segs in segs_6:
        set_diff = segs - encoding_1

        if len(set_diff) == 5:
            encodings[segs] = 6
            segs_6.remove(segs)
            break

    # figure otu encoding for 0,9
    for segs in segs_6:
        set_diff = segs - encoding_4

        if len(set_diff) == 2:
            encodings[segs] = 9
        elif len(set_diff) == 3:
            encodings[segs] = 0

    # figure out encoding for 3
    for segs in segs_5:
        set_diff = segs - encoding_1

        if len(set_diff) == 3:
            encodings[segs] = 3
            segs_5.remove(segs)
            break

    # figure out encoding for 2 and 5
    for segs in segs_5:
        set_diff = segs - encoding_4

        if len(set_diff) == 2:
            encodings[segs] = 5
        elif len(set_diff) == 3:
            encodings[segs] = 2

    out_num = ''

    # decode each digit
    for segs in out_segs:
        decoded = encodings[segs]
        out_num += str(decoded)

    out_num = int(out_num)
    total += out_num

print(total)