from itertools import product

import numpy as np

def get_rot_matrices():
    # rotation matrices for 90 degrees across x, y and z axis
    X = np.array([[1, 0, 0],
                  [0, np.cos(np.pi / 2), -np.sin(np.pi / 2)],
                  [0, np.sin(np.pi / 2), -np.cos(np.pi / 2)]], dtype=int)

    Y = np.array([[np.cos(np.pi / 2), 0, np.sin(np.pi / 2)],
                  [0, 1, 0],
                  [-np.sin(np.pi / 2), 0, np.cos(np.pi / 2)]], dtype=int)

    Z = np.array([[np.cos(np.pi / 2), -np.sin(np.pi / 2), 0],
                  [np.sin(np.pi / 2), np.cos(np.pi / 2), 0],
                  [0, 0, 1]], dtype=int)

    matrices = []
    for mat in [np.eye(3), Y, Y @ Y, Y @ Y @ Y, X, X @ X @ X]:
        matrices.append(mat)
        matrices.append(mat @ Z)
        matrices.append(mat @ Z @ Z)
        matrices.append(mat @ Z @ Z @ Z)

    return matrices

rotation_matrices = get_rot_matrices()

class Scanner:

    points: list[np.ndarray]
    rotations: list[list[np.ndarray]]

    def __init__(self, points):
        self.points = points
        self.rotations = rotate_points(self.points, rotation_matrices)

def parse_input(file_path: str):
    scanners = []
    curr_scanner = None

    for line in open(file_path).readlines():
        line = line.strip()

        if line == '':
            pass
        elif line[:2] == '--':
            curr_scanner = []
            scanners.append(curr_scanner)
        else:
            x, y, z = line.split(',')
            x = int(x)
            y = int(y)
            z = int(z)
            curr_scanner.append(np.array([x, y, z]))

    return [np.array(s) for s in scanners]

def rotate_points(points, matrices):
    res = []
    for mat in matrices:
        rotated = [mat @ point for point in points]
        res.append(rotated)
    return res

def find_matches(s1: Scanner, s2: Scanner, thresh=12):

    all_rotations = s2.rotations

    for rotation in all_rotations:

        for rotated_point, other_point in product(rotation, s1.points):

            diff = other_point - rotated_point

            translated_points = rotation + diff

            concatenation = np.concatenate((s1.points, translated_points))
            uniques = np.unique(concatenation, axis=0)

            if len(concatenation) - len(uniques) >= thresh:
                return diff, uniques

    return None, None

if __name__ == "__main__":

    scanners = parse_input('input_pav.txt')
    scanners = [Scanner(sc) for sc in scanners]

    scanner_positions = []

    main = scanners.pop(0)

    while scanners:

        print(len(scanners))

        scanner = scanners.pop(0)
        diff, match = find_matches(main, scanner)
        if match is not None:
            main.points = match
            scanner_positions.append(diff)
        else:
            scanners.append(scanner)

    print("POSITIONS:")
    for pos in scanner_positions:
        print(list(pos))
