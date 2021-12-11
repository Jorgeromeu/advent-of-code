from itertools import product

import numpy as np

NX = 10
NY = 10
N = 100

def parse_input(file_path: str) -> np.ndarray:
    text = open(file_path).read()
    lines = [s.strip() for s in open(file_path).readlines()]
    nums = [int(x) for x in ''.join(text.split())]
    nums = np.array(nums)
    return nums.reshape((NX, NY))

def neighbor_indices(iy, ix):
    all_neighbor_indices = [(iy + dy, ix + dx) for dy, dx in product([-1, 1, 0], [-1, 1, 0]) if
                            (iy + dy, ix + dx) != (iy, ix)]
    return set([(iy, ix) for iy, ix in all_neighbor_indices if (0 <= iy < NY) and (0 <= ix < NX)])

def step(nums: np.ndarray) -> int:

    num_flashes = 0

    flashing_octopuses = []
    visited = np.zeros(nums.shape, dtype=bool)

    for idx, x in np.ndenumerate(nums):
        nums[idx] += 1
        if nums[idx] > 9:
            num_flashes += 1
            nums[idx] = 0
            flashing_octopuses.append(idx)
            visited[idx] = True

    while flashing_octopuses:
        iy, ix = flashing_octopuses.pop()

        neighbors = neighbor_indices(iy, ix)

        for n in neighbors:
            if not visited[n]:
                nums[n] += 1
                if nums[n] > 9:
                    num_flashes += 1
                    flashing_octopuses.append(n)
                    nums[n] = 0
                    visited[n] = True

    return num_flashes

if __name__ == "__main__":
    nums = parse_input('input.txt')
    num_flashes = 0

    print(nums, end='\n\n')
    for i in range(N):
        num_flashes += step(nums)
        print(nums, end='\n\n')

    print(num_flashes)

