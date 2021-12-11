from itertools import product

import numpy as np

NX = 10
NY = 10

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

def step(nums: np.ndarray):

    flashing_octopuses = []
    visited = np.zeros(nums.shape, dtype=bool)

    for idx, x in np.ndenumerate(nums):
        nums[idx] += 1
        if nums[idx] > 9:
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
                    flashing_octopuses.append(n)
                    nums[n] = 0
                    visited[n] = True

if __name__ == "__main__":
    nums = parse_input('input.txt')

    done = False
    i = 0

    while not done:
        step(nums)
        i += 1

        if (nums == 0).all():
            print(i, 'lol')
            done = True
