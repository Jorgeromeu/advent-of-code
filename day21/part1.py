class Dice:
    val: int
    num_rolls: int

    def __init__(self):
        self.val = 1
        self.num_rolls = 0

    def roll(self):
        ans = self.val
        self.val += 1
        self.val = wrap(self.val, 1, 101)
        self.num_rolls += 1
        return ans

class Player:
    pos: int
    score: int

    def __init__(self, initial_pos):
        self.pos = initial_pos
        self.score = 0

    def advance(self, n):
        self.pos = wrap(self.pos + n, 1, 11)
        self.score += self.pos

def wrap(value, lo, hi):
    diff = hi - lo
    return ((value - lo) % diff) + lo

if __name__ == "__main__":

    # example
    # players = [Player(4), Player(8)]

    # mine
    players = [Player(6), Player(7)]
    d = Dice()

    i = 0
    while True:
        p = players[i % 2]

        r1 = d.roll()
        r2 = d.roll()
        r3 = d.roll()

        p.advance(r1 + r2 + r3)

        # check for win
        if p.score >= 1000:
            looser = players[(i+1) % 2]
            print(d.num_rolls * looser.score)
            break

        i += 1