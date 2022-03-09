import matplotlib.pyplot as plt
import numpy as np

def neighbor_indices(iy, ix):
    return [(iy + dy, ix + dx) for dy in [-1, 0, 1] for dx in [-1, 0, 1]]

def neighbors_values(iy, ix, grid, bg):
    len_y, len_x = grid.shape
    return [grid[iy, ix] if (0 <= iy < len_y) and (0 <= ix < len_x) else bg for iy, ix in neighbor_indices(iy, ix)]

class Image:
    arr: np.ndarray
    bg: int

    def __init__(self, arr):
        self.arr = arr
        self.bg = 0

    def step(self, lookup):
        # pad the array according to background
        padded = np.pad(self.arr, 1, constant_values=self.bg)
        self.arr = padded.copy()

        for (iy, ix), _ in np.ndenumerate(self.arr):
            neighbors = neighbors_values(iy, ix, padded, self.bg)
            idx = int(''.join([str(d) for d in neighbors]), base=2)
            self.arr[iy, ix] = lookup[idx]

        self.bg = 1 if self.bg == 0 else 0

    def show(self):
        plt.imshow(self.arr)
        plt.show()
        plt.cla()

def parse(filename: str):
    lines = [s.strip() for s in open(filename).readlines()]
    lookup = np.array([0 if c == '.' else 1 for c in lines[0]])
    img = np.array([[0 if c == '.' else 1 for c in line] for line in lines[2:]])
    return lookup, img

if __name__ == "__main__":
    lookup, img = parse('input.txt')

    img = Image(img)
    img.show()

    for _ in range(70):
        img.step(lookup)
        img.show()

    print(np.count_nonzero(img.arr))
