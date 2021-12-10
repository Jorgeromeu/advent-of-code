# match closing brackets to opening brackets
opening = {')': '(',
           ']': '[',
           '}': '{',
           '>': '<'}

errors = {')': 3, ']': 57, '}': 1197, '>': 25137}

opening_brackets = {'(', '[', '{', '<'}
closing_brackets = {')', ']', '}', '>'}

def check_line(line: str) -> int:
    stack = []

    for char in line:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            top = stack.pop()

            if top != opening[char]:
                return errors[char]

    # no errors
    return 0

if __name__ == "__main__":

    lines = [s.strip() for s in open('input.txt').readlines()]

    score = 0

    for line in lines:
        score += check_line(line)

    print(score)
