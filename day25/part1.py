import numpy as np

def parse_input(filename: str):
    lines = [s.strip() for s in open(filename).readlines()]
    chars = [list(line) for line in lines]
    return np.array(chars)

def step(arr: np.ndarray):

    height, width = arr.shape

    initial_copy = arr.copy()

    # first pass
    for (iy, ix), c in np.ndenumerate(initial_copy):
        if c == '>':

            next_x = (ix+1) % width

            if initial_copy[iy, next_x] == '.':
                arr[iy, next_x] = '>'
                arr[iy, ix] = '.'

    second_copy = arr.copy()

    # second pass
    for (iy, ix), c in np.ndenumerate(second_copy):
        if c == 'v':

            next_y = (iy+1) % height

            if second_copy[next_y, ix] == '.':
                arr[next_y, ix] = 'v'
                arr[iy, ix] = '.'

    return (initial_copy == arr).all()

def display(arr):
    for line in arr:
        for char in line:
            print(char, end='')
        print()

if __name__ == "__main__":

    arr = parse_input('input.txt')

    done = False

    i = 0
    while not done:
        done = step(arr)
        print(f'After {i+1} steps')
        i += 1

    # answer is 579
    display(arr)