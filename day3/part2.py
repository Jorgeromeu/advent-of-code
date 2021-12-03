lines = open('input.txt').readlines()
num_bits = len(lines[0]) - 1

# create a stripped copy of the list for o2 and co2
nums_o2 = list(map(lambda s: s.strip(), lines))
nums_co2 = list(map(lambda s: s.strip(), lines))

def count_bits(nums, bit_idx):
    count_0 = 0
    count_1 = 0
    for num in nums:
        if num[bit_idx] == '0':
            count_0 += 1
        else:
            count_1 += 1
    return count_0, count_1

def solve(nums, criterion):

    num_bits = len(nums[0])

    for curr_bit in range(num_bits):

        # count the amount of 0s and 1s in the column
        count_0, count_1 = count_bits(nums, curr_bit)

        to_be_removed = []

        # filter the list
        for num in nums:
            
            if criterion(num[curr_bit], count_0, count_1):
                to_be_removed.append(num)

        # remove the filtered items
        for num in to_be_removed:
            if len(nums) > 1:
                nums.remove(num)

    return nums[0]

def o2_criterion(bit, count_0, count_1):
    most_frequent_value = '1' if count_0 > count_1 else '0'
    return bit == most_frequent_value

def co2_criterion(bit, count_0, count_1):
    most_infrequent_value = '1' if count_0 <= count_1 else '0'
    return bit == most_infrequent_value

if __name__ == '__main__':


    o2_gen = solve(nums_o2, o2_criterion)
    co2_scrub = solve(nums_co2, co2_criterion)

    print('o2', o2_gen)
    print('co2', co2_scrub)

    o2_gen = int(o2_gen, base=2)
    co2_scrub = int(co2_scrub, base=2)

    print(co2_scrub * o2_gen)