import matplotlib.pyplot as plt
import numpy as np

def read_input(file_path):
    coords = []
    folds = []

    for line in open(file_path):
        line = line.strip()

        if line == '':
            continue
        if line[0].isnumeric():
            x, y = line.split(',')
            coords.append((int(x), int(y)))
        elif line[0] == 'f':
            axis = line[11]
            pos = int(line[13:])
            folds.append((axis, int(pos)))

    return coords, folds

# convert list of points to numpy array (for viz)
def to_array(coords):
    len_x = max(coord[0] for coord in coords)
    len_y = max(coord[1] for coord in coords)
    arr = np.zeros((len_y + 1, len_x + 1))

    for x, y in coords:
        arr[y, x] = 1

    return arr

def fold(axis, pos, coords):
    ret = []

    for x, y in coords:

        if axis == 'y':

            if y < pos:
                ret.append((x, y))
            elif y > pos:
                reflected_y = pos - (y - pos)
                ret.append((x, reflected_y))

        elif axis == 'x':

            if x < pos:
                ret.append((x, y))
            elif x > pos:
                reflected_x = pos - (x - pos)
                ret.append((reflected_x, y))
    return ret

if __name__ == "__main__":
    coords, folds = read_input('input.txt')

    # do the first fold
    axis, pos = folds[0]
    coords = fold(axis, pos, coords)
    arr = to_array(coords)
    print(np.count_nonzero(arr))

    for axis, pos in folds[1:]:
        coords = fold(axis, pos, coords)

    arr = to_array(coords)
    plt.imshow(arr)
    plt.show()
