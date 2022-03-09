import random

from day24.alu import ALU

def monad(num: str):
    nums1 = [1, 1, 1, 1, 26, 1, 1, 26, 26, 26, 26, 1, 26, 26]  # div z
    nums2 = [10, 10, 12, 11, 0, 15, 13, -12, -15, -15, -4, 10, -5, -12]  # add x
    nums3 = [12, 10, 8, 4, 3, 10, 6, 13, 8, 1, 7, 6, 9, 9]  # add y
    digits = [int(c) for c in num]

    acc = 0

    # foreach digit
    for i in range(14):

        x = acc % 26

        # divide accumulator by 26 or 1
        acc //= nums1[i]

        flag = x + nums2[i] != digits[i]

        y = 26 if flag else 1

        acc *= y

        y = (digits[i] + nums3[i]) if flag else 0

        acc += y

    return acc

def test_monad(monad):

    for it in range(100):
        num = ''.join([str(random.randrange(1, 10)) for _ in range(14)])

        alu = ALU(num)
        alu.exec_prog_from_file('input.txt')
        alu_res = alu.mem['z']
        my_res = monad(num)

        if my_res != alu_res:
            print(it, num)
            return False

    return True

if __name__ == "__main__":

    print(test_monad(monad))

    pass
