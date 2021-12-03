import math

data = open('input.txt').readlines()

windows = []

for i, line in enumerate(data):

    if i > (len(data) - 3):
        break

    a = int(data[i+0])
    b = int(data[i+1])
    c = int(data[i+2])

    windows.append(a+b+c)

# count the amount of increases
count = 0
prev = windows[0]
for measurement in windows[1:]:
    if measurement > prev:
        count += 1
    prev = measurement

print('result:', count)

