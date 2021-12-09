import numpy as np
from collections import defaultdict

class UnionFind:
    items: list
    parent: dict
    rank: dict

    def __init__(self, items: list):
        self.items = items
        self.parent = {it: it for it in items}
        self.rank = {it: 0 for it in items}

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b) -> bool:
        aRep = self.find(a)
        bRep = self.find(b)

        if aRep == bRep:
            return False

        if self.rank[a] > self.rank[b]:
            self.parent[bRep] = aRep
        else:
            self.parent[aRep] = bRep

            if self.rank[a] == self.rank[b]:
                self.rank[bRep] += 1

        return True

    def clusters(self) -> list:

        res = defaultdict(lambda: [])

        for it in self.items:
            res[self.find(it)].append(it)

        return list(res.values())

def parse_input(file_path: str):
    text = open(file_path).read()
    lines = [s.strip() for s in open(file_path).readlines()]

    len_x = len(lines[0])
    len_y = len(lines)
    nums = [int(x) for x in ''.join(text.split())]
    nums = np.array(nums)
    nums = nums.reshape((len_y, len_x))
    return len_x, len_y, nums

def neighbor_heights(iy: int, ix: int, nums: np.ndarray):
    clamped_neighbor_indices = neighbor_indices(iy, ix, nums)
    return [nums[y, x] for y, x in clamped_neighbor_indices]

def neighbor_indices(iy: int, ix: int, nums: np.ndarray):
    len_y, len_x = nums.shape
    neighbor_indices = [(iy + 1, ix), (iy - 1, ix), (iy, ix - 1), (iy, ix + 1)]
    return [(y, x) for y, x in neighbor_indices if (0 <= y < len_y) and (0 <= x < len_x)]

if __name__ == "__main__":

    len_x, len_y, nums = parse_input('input.txt')

    # get all low-points
    lo_points = []
    for iy, ix in np.ndindex(nums.shape):
        if nums[iy, ix] < min(neighbor_heights(iy, ix, nums)):
            lo_points.append((iy, ix))

    # boolean array, true means the point is in a basin
    basins = (nums != 9)

    # unionfind of all points in array
    uf = UnionFind(list(np.ndindex(nums.shape)))

    while lo_points:

        iy, ix = lo_points.pop()

        neighbors = neighbor_indices(iy, ix, nums)

        for n in neighbors:

            # if the neighbor is also a basin union them
            if basins[n]:
                if uf.union(n, (iy, ix)):
                    lo_points.append(n)

    # print the product of the largest clusters
    sizes = []
    for cluster in uf.clusters():
        sizes.append(len(cluster))

    sizes = sorted(sizes, reverse=True)
    print(sizes[0] * sizes[1] * sizes[2])
