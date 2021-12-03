nums = [s.strip() for s in open('input_small.txt').readlines()]
num_bits = len(nums[0])

# for each bit-index keep track of how many 1s and 0s we find
counts = [{'0': 0, '1': 0} for _ in range(num_bits)]

for line in nums:
    for (i, b) in enumerate(line):
        counts[i][b] += 1

gamma = []
epsilon = []
for freq in counts:

    if freq['0'] > freq['1']:
        gamma.append('0')
        epsilon.append('1')
    else:
        gamma.append('1')
        epsilon.append('0')

gamma = int(''.join(gamma), base=2)
epsilon = int(''.join(epsilon), base=2)

print(gamma * epsilon)