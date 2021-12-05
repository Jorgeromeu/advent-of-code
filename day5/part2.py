import numpy as np
import matplotlib.pyplot as plt
import re

lines = [s.strip() for s in open('input.txt').readlines()]

points = np.zeros((len(lines), 4), dtype=int)
for i, line in enumerate(lines):
    p1, p2 = re.split(' -> ', line)
    x1, y1 = p1.split(',')
    x2, y2 = p2.split(',')
    points[i][0] = int(x1)
    points[i][1] = int(y1)
    points[i][2] = int(x2)
    points[i][3] = int(y2)

max_x = np.max((points[:,0], points[:,2]))
max_y = np.max((points[:,1], points[:,3]))

table = np.zeros((max_y+1, max_x+1), dtype=int)

for x1, y1, x2, y2 in points:

    # horizontal line
    if x1 == x2:
        y1, y2 = sorted((y1, y2))                
        table[y1:y2+1, x1] += 1

    # vertical line 
    elif y1 == y2:
        x1, x2 = sorted((x1, x2))                
        table[y1, x1:x2+1] += 1

    # diagonal lines
    else:
        line_len = abs(x1 - x2)
        dir_y = (y2 - y1) // line_len
        dir_x = (x2 - x1) // line_len

        for i in range(line_len + 1):
            table[y1 + i*dir_y, x1 + i*dir_x] += 1



plt.imshow(table)
plt.savefig('result.png', bbox_inches='tight')

print(np.count_nonzero(table >= 2))