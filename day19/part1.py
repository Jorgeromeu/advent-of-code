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
    for mat in [np.eye(3), Y, Y@Y, Y@Y@Y, X, X@X@X]:
        matrices.append(mat)
        matrices.append(mat @ Z)
        matrices.append(mat @ Z @ Z)
        matrices.append(mat @ Z @ Z @ Z)

    return matrices

rotation_matrices = get_rot_matrices()

print(rotation_matrices)

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

def find_matches(s1: np.ndarray, s2: np.ndarray, thresh=12):

    all_rotations = rotate_points(s2, rotation_matrices)
    for rotation in all_rotations:

        for rotated_point, other_point in product(rotation, s1):

            diff = other_point - rotated_point

            translated_points = rotation + diff

            concatenation = np.concatenate((s1, translated_points))
            uniques = np.unique(concatenation, axis=0)

            if len(concatenation) - len(uniques) >= thresh:
                return uniques

    return None

if __name__ == "__main__":

    scanners = parse_input('input_pav.txt')
    rotation_matrices = get_rot_matrices()

    main = scanners[0]

    remaining_scanners = scanners[1:]

    while remaining_scanners:

        print(len(remaining_scanners))

        scanner = remaining_scanners.pop(0)
        match = find_matches(main, scanner)
        if match is not None:
            main = match
        else:
            remaining_scanners.append(scanner)


    print(len(main))
