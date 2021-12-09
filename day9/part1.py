import matplotlib.pyplot as plt
import numpy as np

file_path = 'input.txt'

text = open(file_path).read()
lines = [s.strip() for s in open(file_path).readlines()]

len_x = len(lines[0])
len_y = len(lines)

nums = [int(x) for x in ''.join(text.split())]
nums = np.array(nums)
nums = nums.reshape((len_y, len_x))

def neighbors(iy, ix, nums):
    neighbor_indices = [(iy + 1, ix), (iy - 1, ix), (iy, ix - 1), (iy, ix + 1)]
    clamped_neighbor_indices = [(y, x) for y, x in neighbor_indices if (0 <= y < len_y) and (0 <= x < len_x)]
    return [nums[y, x] for y, x in clamped_neighbor_indices]

risk = 0

for iy, ix in np.ndindex(nums.shape):

    # check if is low point
    if nums[iy, ix] < min(neighbors(iy, ix, nums)):
        risk += nums[iy, ix] + 1

print(risk)

plt.imshow(nums)
plt.colorbar()
plt.show()
