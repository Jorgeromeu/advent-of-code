lines = [line.strip() for line in open('input.txt').readlines()]

# number lengths    
lens = {2, 3, 4, 7}

count = 0

for line in lines:
    nums, displayed = line.split('|')

    # strip and split
    nums = nums.strip().split(' ')
    displayed = displayed.strip().split(' ')

    for number in displayed:

        if len(number) in lens:
            count += 1    

print(count)