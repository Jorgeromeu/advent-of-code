lines = open('input.txt').readlines()

xpos = 0
depth = 0

for line in lines:
    direction, number = line.split(' ')
    number = int(number)

    if direction == 'forward':
        xpos += number
    elif direction == 'down':
        depth += number
    elif direction == 'up':
        depth -= number

# anser is product of xposition and depth
print(xpos * depth)
