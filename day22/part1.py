from dataclasses import dataclass

from typing import List

def intersection(a_lo, a_hi, b_lo, b_hi) -> (int, int):
    # sort lines by lo point
    left, right = sorted([(a_lo, a_hi), (b_lo, b_hi)])

    # left contains right
    # +-----+
    #   +-+
    if left[1] >= right[1]:
        return right[0], right[1]

    # left intersects right
    # +-----+
    #   +------+
    if right[0] < left[1]:
        return right[0], left[1]

    # else there is no intersection
    # +---+
    #        +---+
    return None

@dataclass
class Box:
    xlo: int
    xhi: int
    ylo: int
    yhi: int
    zlo: int
    zhi: int

    positive: bool

    def signed_area(self):
        abs_area = self.volume()
        return abs_area if self.positive else -abs_area

    def volume(self):
        return (self.xhi - self.xlo + 1) * (self.yhi - self.ylo + 1) * (self.zhi - self.zlo + 1)

    def intersection(self, other):
        x_line = intersection(self.xlo, self.xhi, other.xlo, other.xhi)
        y_line = intersection(self.ylo, self.yhi, other.ylo, other.yhi)
        z_line = intersection(self.zlo, self.zhi, other.zlo, other.zhi)

        if x_line and y_line and z_line:
            return Box(x_line[0], x_line[1], y_line[0], y_line[1], z_line[0], z_line[1], True)

        return None

    def pav_intersection(self, other):
        xlo = max(self.xlo, other.xlo)
        xhi = min(self.xhi, other.xhi)
        ylo = max(self.ylo, other.ylo)
        yhi = min(self.yhi, other.yhi)
        zlo = max(self.zlo, other.zlo)
        zhi = min(self.zhi, other.zhi)

        return Box(xlo, xhi, ylo, yhi, zlo, zhi, not self.positive)

    def in_cube(self, lo, hi):
        x_in = self.xlo >= lo and self.xhi <= hi
        y_in = self.ylo >= lo and self.yhi <= hi
        z_in = self.zlo >= lo and self.zhi <= hi
        return x_in and y_in and z_in

def subdivide(boxes: List[Box]):
    xcoords = sorted([b.xlo for b in boxes] + [b.xhi for b in boxes])
    ycoords = sorted([b.ylo for b in boxes] + [b.yhi for b in boxes])
    zcoords = sorted([b.zlo for b in boxes] + [b.zhi for b in boxes])
    n = len(xcoords)

    assert len(xcoords) == len(ycoords) == len(zcoords)

    subdivided = []

    for xi in range(n - 1):
        for yi in range(n - 1):
            for zi in range(n - 1):
                x_nxt = xcoords[xi + 1]
                y_nxt = ycoords[yi + 1]
                z_nxt = xcoords[zi + 1]

                if {xi, xi + 1} & {yi, yi + 1} & {zi, zi + 1} != set():
                    subdivided.append(
                        Box(xcoords[xi], xcoords[xi + 1], ycoords[yi], ycoords[yi + 1], zcoords[zi], zcoords[zi + 1],
                            True))

    return subdivided

def parse_input(file_path):
    lines = [s.strip() for s in open(file_path)]
    boxes = []
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

        positive = True if cmd == 'on' else False

        boxes.append(Box(xlo, xhi, ylo, yhi, zlo, zhi, positive))

    return boxes

if __name__ == "__main__":

    instructions = parse_input('input_small.txt')

    boxes = []

    for box in instructions:
        temp = []

        if box.positive:
            temp.append(box)

        for other in boxes:
            intersect = other.pav_intersection(other)
            if intersect:
                temp.append(intersect)

        boxes += temp

    print(boxes)

    score = sum(b.area() for b in boxes)
    print(score)
