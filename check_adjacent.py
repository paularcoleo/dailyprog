# #288 [Hard] Adjacent Numbers Solution Checker
# https://www.reddit.com/r/dailyprogrammer/comments/58n2ca/20161021_challenge_288_hard_adjacent_numbers/
# Checks arbitrary grids, returns sum if valid, returns problems if not
# now with super descriptive comments

from itertools import permutations


def grid(grid):
    # Takes in a grid as a set of nested lists with single digit strs
    score = 0
    for y, row in enumerate(grid):
        # find the sum of the row, add it to the score
        score += sum(int(i) for i in row) 
        for x, num in enumerate(row):
            # generates all possible up/down/diagonal moves
            # that way I can loop through the moves, find the
            # values in the adjacent cells, and add them to the
            # 'adjs' set to compaire to the required set
            moves = [-1, 0, 1, -1, 0, 1] 
            sqs = permutations(moves, 2) 
            adjs = set() 
            for sq in sqs:
                if sq == (0,0):
                    continue
                else:
                    # the try-except block here circumvents lengthy if-else
                    # statements that would need to be run in order to avoid
                    # index errors/unwanted values when you approach the edges
                    # and corners of the grid
                    try:
                        # using set unions to add the values up/down/diagonal
                        # from the initial number, since repeated numbers
                        # don't matter!
                        adjs = adjs | {int(grid[y+sq[0]][x+sq[1]])}
                    except IndexError:
                        # again, if a move is invalid (edge of grid), just move on
                        continue
            # make a set of the values between 1 and the number being checked,
            # which is the criteria for a valid solution. do a set subtraction
            # from the required set, and if all the required set was found in
            # the adjacent set, the resultant set 'rem' for 'remaining' should
            # be empty
            needed = set(range(1,int(num)))
            rem = needed-adjs
            # if the rem set is not empty, it means that there is a missing value
            # so, print out a basic message with the x,y value of the missing number
            # and highlight which number is missing from the required set
            if not len(rem) == 0:
                print("Erorr at {},{}: {} not connected to {}".format(
                    x+1, # +1 so that the counting starts at 1, not 0
                    y, # don't ask me why I don't need to put +1 on y because I don't know
                    num,
                    str(rem)))
                # return 0 because the board is invalid, therefore should not have a score!
                return 0 
    # if it made it all the way through, return the score!
    return score


# this function is just a quick shorthand to handle copy-pasta data.
# on /r/dailyprogrammer, submission outputs are given in plain text,
# so pasting it in as a multi-line string and then just removing all
# whitespace and using a list comp with splitlines to get the desired
# nested list input for grid() was the easiest solution. It's not 
# beautiful, but it's concise.
def format_grid(grid):
    return [list(x) for x in grid.replace(' ', '').splitlines()]

test ='''
1 2 3 1 2 3 1 2 3 1
3 8 5 9 8 5 9 8 5 2
4 7 6 4 7 6 4 7 6 4
1 2 3 1 2 3 1 2 3 1
3 8 5 9 8 5 9 8 5 2
4 7 6 4 7 6 4 7 6 4
1 2 3 1 2 3 1 2 3 1
3 8 5 9 8 5 9 8 5 2
4 6 7 4 6 7 4 6 7 4
1 2 3 1 2 3 1 2 3 1
'''

print(grid(format_grid(test)))
