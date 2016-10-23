# #288 [Hard] Adjacent Numbers Solution Checker
# https://www.reddit.com/r/dailyprogrammer/comments/58n2ca/20161021_challenge_288_hard_adjacent_numbers/
# Checks arbitrary grids, returns sum if valid, returns problems if not

from itertools import permutations


def grid(grid):
    score = 0
    for y, row in enumerate(grid):
        score += sum(int(i) for i in row)
        for x, num in enumerate(row):
            moves = [-1, 0, 1, -1, 0, 1]
            sqs = permutations(moves, 2)
            adjs = set()
            for sq in sqs:
                if sq == (0,0):
                    continue
                else:
                    try:
                        adjs = adjs | {int(grid[y+sq[0]][x+sq[1]])}
                    except IndexError:
                        continue
            needed = set(range(1,int(num)))
            rem = needed-adjs
            if not len(rem) == 0:
                print("Erorr at {},{}: {} not connected to {}".format(
                    x+1,
                    y,
                    num,
                    str(rem)))
                return 0
    return score


def format_grid(grid):
    return [list(x) for x in grid.replace(' ', '').splitlines()]

test ='''
1 4 5 1 5 4 1 5 4 1
2 3 6 2 6 3 2 6 3 2
2 5 8 2 8 7 2 8 5 2
1 4 7 1 5 4 1 7 4 1
3 6 9 3 9 8 3 9 6 3
2 5 8 2 7 6 2 8 5 2
1 4 7 1 5 4 1 7 4 1
3 6 8 3 8 7 3 8 6 3
2 5 7 2 6 5 2 7 5 2
1 3 4 1 4 3 1 4 3 1
'''

print(grid(format_grid(test)))
