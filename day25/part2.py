from collections import defaultdict, Counter
from itertools import product

def wrap(value, lo, hi):
    diff = hi - lo
    return ((value - lo) % diff) + lo

if __name__ == "__main__":

    # game state format:
    # p1_po2, p2_pos, p1_score, p2_score

    # initial reality
    state_counts = defaultdict(lambda: 0)

    # my input
    state_counts[(6, 7, 0, 0)] = 1

    # example
    # state_counts[(4, 8, 0, 0)] = 1

    # keep track of wins
    wins = {1: 0, 2: 0}

    # get all possible roll sums and their counts
    roll_counts = dict(Counter([sum(roll) for roll in product([1, 2, 3], [1, 2, 3], [1, 2, 3])]))

    curr_player = 1

    while sum(state_counts.values()) != 0:

        print(f'player: {curr_player}, {sum(state_counts.values())}')

        # make a copy of previous state counts
        prev_states = state_counts.copy()

        for state, state_count in prev_states.items():

            if state_count == 0:
                continue

            p1_pos, p2_pos, p1_score, p2_score = state

            # reduce the count of the states
            state_counts[state] -= state_count

            # for each possible roll combination create the alternate realities
            for roll, num_variants in roll_counts.items():

                if curr_player == 1:
                    new_p1_pos = wrap(p1_pos + roll, 1, 11)
                    new_p1_score = p1_score + new_p1_pos

                    # check for win
                    if new_p1_score >= 21:
                        wins[1] += state_count * num_variants
                    else:
                        state_counts[(new_p1_pos, p2_pos, new_p1_score, p2_score)] += state_count * num_variants

                elif curr_player == 2:
                    new_p2_pos = wrap(p2_pos + roll, 1, 11)
                    new_p2_score = p2_score + new_p2_pos

                    # check for win
                    if new_p2_score >= 21:
                        wins[2] += state_count * num_variants
                    else:
                        state_counts[(p1_pos, new_p2_pos, p1_score, new_p2_score)] += state_count * num_variants

        # increment current player
        curr_player = wrap(curr_player + 1, 1, 3)


    print("wins")
    print(wins)
    print(max(wins.values()))
