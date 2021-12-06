import numpy as np

school = open('input.txt').read().strip().split(',')
school = list(map(int, school))

num_days = 256

# keep track of how many fish have a specific cycle nuber
counts = np.zeros(9, dtype=int)

# keep track of the quantity of each age rather than each fish
for fish in school:
    counts[fish] += 1

for day in range(num_days):

    counts_cp = counts.copy()

    # quantity of i becomes quantity of i+1
    for i in range(0, 8):
        counts[i] = counts_cp[i+1]
    
    # the amount of newborns is the amount of 6s in the previous iteration
    counts[8] = counts_cp[0];

    # all the 0s become 6s
    counts[6] += counts_cp[0]

# print the total amount of fish
print(sum(counts))