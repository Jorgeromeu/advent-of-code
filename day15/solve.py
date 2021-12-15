import math
from queue import PriorityQueue

import matplotlib.pyplot as plt
import numpy as np

def parse_input(file_path: str) -> np.ndarray:
    text = open(file_path).read()
    lines = [s.strip() for s in open(file_path).readlines()]

    len_x = len(lines[0])
    len_y = len(lines)
    nums = [int(x) for x in ''.join(text.split())]
    nums = np.array(nums)
    nums = nums.reshape((len_y, len_x))
    return nums

# get the indices of the neighbors in the grid
def neighbor_indices(iy: int, ix: int, nums: np.ndarray):
    len_y, len_x = nums.shape
    all_neighbor_indices = [(iy + 1, ix), (iy - 1, ix), (iy, ix - 1), (iy, ix + 1)]
    return [(y, x) for y, x in all_neighbor_indices if (0 <= y < len_y) and (0 <= x < len_x)]

# wrap value in range [lo, hi) with modular arithmetic
def wrap(value, lo=1, hi=10):
    diff = hi - lo
    return ((value - lo) % diff) + lo

# extend the grid (for part 2)
def extend_grid(grid, ny, nx):
    extended_row = np.concatenate(tuple(wrap(grid + i) for i in range(nx)), axis=1)
    extended_grid = np.concatenate(tuple(wrap(extended_row + i) for i in range(ny)), axis=0)
    return extended_grid

if __name__ == "__main__":

    # construct graph
    graph = parse_input('input.txt')
    # graph = extend_grid(graph, 5, 5) (part 2)

    # distance to all nodes is inf, except start which is 0
    dist = np.full(graph.shape, math.inf)
    dist[0, 0] = 0

    # initialize priority Queue
    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    while not pq.empty():

        cost, vertex = pq.get()

        # for each neighbor, relax weight edges
        for neighbor in neighbor_indices(vertex[0], vertex[1], graph):

            relaxed_weight = cost + graph[neighbor]

            if relaxed_weight < dist[neighbor]:
                dist[neighbor] = relaxed_weight
                pq.put((relaxed_weight, neighbor))

    plt.imshow(dist)
    plt.show()

    # print distance to ending node
    print(dist[-1, -1])
