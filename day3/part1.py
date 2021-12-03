lines = open('input.txt').readlines()


num_bits = len(lines[0][:-1])

# for each bit-index keep track of how many 1s and 0s we find
frequencies = [{'0': 0, '1': 0} for _ in range(num_bits)]

for line in lines:
    for (i, b) in enumerate(line[:-1]):
        frequencies[i][b] += 1

gamma = []
epsilon = []
for freq in frequencies:

    if freq['0'] > freq['1']:
        gamma.append('0')
        epsilon.append('1')
    else:
        gamma.append('1')
        epsilon.append('0')

gamma = int(''.join(gamma), base=2)
epsilon = int(''.join(epsilon), base=2)

print(gamma * epsilon)

