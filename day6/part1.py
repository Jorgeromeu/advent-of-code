school = open('input.txt').read().strip().split(',')
school = list(map(int, school))

num_days = 256

for day in range(num_days):

    num_newborns = 0

    for (i, fish) in enumerate(school):

        # if fish reaches their cycle reset and spawn a new one
        if fish == 0:
            school[i] = 6
            num_newborns += 1

        # otherwise just decrement
        else:
            school[i] -= 1

    # add all the newborn fish to the list
    for _ in range(num_newborns):
        school.append(8)

    print(day)

print(len(school))
    
