from collections import defaultdict

def read_input(file_path):
    lines = [s.strip() for s in open(file_path).readlines()]

    seq = lines[0]
    rules = dict()

    for line in lines[2:]:
        pair, char = line.split(' -> ')
        rules[pair] = char

    return seq, rules

def step(pairs, counts, rules):
    pairs_copy = pairs.copy()

    for pair, cnt in pairs.items():
        pairs_copy[pair] -= cnt
        pairs_copy[pair[0]+rules[pair]] += cnt
        pairs_copy[rules[pair]+pair[1]] += cnt
        counts[rules[pair]] += cnt

    return pairs_copy

if __name__ == "__main__":

    seq, rules = read_input('input.txt')

    # count the pairs
    pair_counts = defaultdict(lambda: 0)
    for i, c in enumerate(seq[:-1]):
        c_next = seq[i + 1]
        pair_counts[c + c_next] += 1

    # count how many times each individual pair shows up
    char_counts = defaultdict(lambda: 0)
    for c in seq:
        char_counts[c] += 1

    # do 10 iterations
    for i in range(40):
        pair_counts = step(pair_counts, char_counts, rules)

    # most common - least common
    quantities = sorted(char_counts.values(), reverse=True)
    print(quantities[0] - quantities[-1])
