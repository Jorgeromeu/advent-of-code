lines = open('input.txt').readlines()

xpos = 0
depth = 0
aim = 0

for line in lines:
    direction, number = line.split(' ')
    number = int(number)

    if direction == 'forward':
        xpos += number
        depth += aim * number
    elif direction == 'down':
        aim += number
    elif direction == 'up':
        aim -= number

# anser is product of xposition and depth
print(xpos * depth)
