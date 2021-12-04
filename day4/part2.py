import numpy as np
import re

class Board:
    nums: np.ndarray
    marks: np.ndarray

    def __init__(self, numbers: np.ndarray):
        self.nums = numbers.reshape((5,5))
        self.marks = np.zeros((5,5))

    def mark(self, n):
        self.marks[self.nums == n] = 1

    def score(self, draw):
        return np.sum(self.nums[self.marks == 0]) * draw

    def won(self):
        row_sums = np.sum(self.marks, axis=0)
        col_sums = np.sum(self.marks, axis=1)
        return np.max(row_sums) == 5 or np.max(col_sums) == 5



lines = [s.strip() for s in open('input_small.txt').readlines()]

# get the numbers drawn
draws = [int(x) for x in lines[0].split(',')]

# get lists of boards
boards = []

for i in range(2, len(lines), 6):
    numbers = [re.split(r'\s+', lines[i+j]) for j in range(5)]
    numbers = np.array(numbers)
    numbers = numbers.astype(int)
    boards.append(Board(numbers))

last_win = None

for draw in draws:
    
    to_be_removed = []
    
    for board in boards:

        # mark the board with the drawn number
        board.mark(draw)

        if board.won():
            last_win = board.score(draw)
            to_be_removed.append(board)

    for board in to_be_removed:
        boards.remove(board)
    

print(last_win)