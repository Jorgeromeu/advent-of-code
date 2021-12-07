import numpy as np

crab_pos = np.array([int(n) for n in open('input.txt').read().strip().split(',')])

def fuel_cost(s, t):
    return abs(s - t)

# the target is the median
median = round(np.median(crab_pos))

# compute total cost
total_cost = np.sum(fuel_cost(crab_pos, median))
print(total_cost)