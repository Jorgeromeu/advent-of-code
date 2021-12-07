import numpy as np

crab_pos = np.array([int(n) for n in open('input.txt').read().strip().split(',')])

def sum_up_to(n):
    return (n * (n+1)) // 2

def fuel_cost(s, t):
    return sum_up_to(abs(s - t))

# take mean and mean+1 as possible positions
mean_lo = int(np.mean(crab_pos))
mean_hi = mean_lo + 1

# take whichever is less costly
cost_lo = np.sum(fuel_cost(crab_pos, mean_hi))
cost_hi = np.sum(fuel_cost(crab_pos, mean_lo))

# print result
print(min(cost_hi, cost_lo))
