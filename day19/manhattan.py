import numpy as np

def manhattan(p, q):
    return np.sum(np.abs(p - q))

if __name__ == "__main__":

    points = [np.array(eval(line), dtype=int) for line in open('points_pav.txt').readlines()]

    maxdist = 0

    for p in points:
        for q in points:
            if (p != q).all():
                maxdist = max(maxdist, manhattan(p, q))

    print(maxdist)
