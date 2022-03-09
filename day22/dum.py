import numpy as np

class Grid:
    arr: np.ndarray
    min_coord: int
    max_coord: int

    def __init__(self, min_coord, max_coord):
        length = max_coord - min_coord
        self.arr = np.zeros(shape=(length, length, length), dtype=bool)
        self.min_coord = min_coord
        self.max_coord = max_coord

    def _test_range(self, x, y, z):
        assert (min_coord <= x < max_coord) and (min_coord <= y <= max_coord) and (min_coord <= z <= max_coord)

    def get(self, x, y, z):
        self._test_range(x, y, z)
        return self.arr[y-min_coord, x-min_coord, z-min_coord]

    def set(self, x, y, z, val):
        self._test_range(x, y, z)
        self.arr[y-min_coord, x-min_coord, z-min_coord] = val

def parse_input(file_path):

    min_coord = 1e100
    max_coord = -1e100

    lines = [s.strip() for s in open(file_path)]
    instructions = []
    for line in lines:
        cmd, remainder = line.split(' ')
        xrange, yrange, zrange = remainder.split(',')
        xlo, xhi = xrange.split('=')[1].split('..')
        ylo, yhi = xrange.split('=')[1].split('..')
        zlo, zhi = xrange.split('=')[1].split('..')

        xlo = int(xlo)
        ylo = int(ylo)
        zlo = int(zlo)
        xhi = int(xhi)
        yhi = int(yhi)
        zhi = int(zhi)

        # keep running max/min x,y,z for the size of the grid
        min_coord = min(min_coord, xlo, ylo, zlo)
        max_coord = max(max_coord, xhi, yhi, zhi)

        instructions.append([cmd, xlo, xhi, ylo, yhi, zlo, zhi])

    return (min_coord, max_coord), instructions

if __name__ == "__main__":
    (min_coord, max_coord), instructions = parse_input('input.txt')

    grid = Grid(min_coord, max_coord)

    for instr in instructions:

        match instr:
            case ['on', xlo, xhi, ylo, yhi, zlo, zhi]:
                print(xlo, xhi)
            case['off', xlo, xhi, ylo, yhi, zlo, zhi]:
                print(xlo, xhi)
