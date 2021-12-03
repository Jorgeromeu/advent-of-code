import math

data = open('./input.txt').readlines()

count = 0
prev = int(data[0])

for line in data[1:]:
    measurement = int(line)
    if measurement > prev:
        count += 1
    prev = measurement
    print(measurement, count)

print('result:', count)

