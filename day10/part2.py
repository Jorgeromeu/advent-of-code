from functools import reduce

# match closing brackets to opening brackets
opening = {')': '(',
           ']': '[',
           '}': '{',
           '>': '<'}
closing = {'(': ')',
           '[': ']',
           '{': '}',
           '<': '>'}

errors = {')': 1, ']': 2, '}': 3, '>': 4}

opening_brackets = {'(', '[', '{', '<'}
closing_brackets = {')', ']', '}', '>'}

def check_line(line: str) -> list:
    stack = []

    for char in line:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            top = stack.pop()

            if top != opening[char]:
                return []

    # no errors
    return stack

def sequence_score(seq):
    return reduce(lambda acc, x: acc*5 + x, [errors[closing[char]] for char in seq], 0)

if __name__ == "__main__":

    lines = [s.strip() for s in open('input.txt').readlines()]

    scores = []

    for line in lines:
        closing_seq = list(reversed(check_line(line)))
        if closing_seq:
            score = sequence_score(closing_seq)
            scores.append(score)

    # print middle element
    print(sorted(scores)[len(scores)//2])

