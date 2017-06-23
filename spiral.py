# Daily Programmer # 320 - Spiral Ascension
# https://www.reddit.com/r/dailyprogrammer/comments/6i60lr/20170619_challenge_320_easy_spiral_ascension/

import sys

def turn(cycler, i, j):
    cycler += 1
    di = order[cycler % 5]
    ni, nj = i + di[0], j + di[1]
    return ni, nj, di, cycler 

def spiral(n):
    swirl = [[0 for k in range(n)] for l in range(n)]
    num, cycler = 1, 0
    i, j = 0 - order[0][0], 0 - order[0][1]
    di = order[cycler % 4]
    while num <= n ** 2:
        ni, nj = i + di[0], j + di[1]
        try:
            if swirl[ni][nj] == 0:
                swirl[ni][nj] = num
            else:
                ni, nj, di, cycler = turn(cycler, i, j)
                swirl[ni][nj] = num
        except IndexError:
            ni, nj, di, cycler = turn(cycler, i, j)
            swirl[ni][nj] = num
        num += 1
        i, j = ni, nj
    for row in swirl:
        print([str(z).rjust(len(str(n**2))) for z in row])

if __name__ == '__main__':
    n = int(sys.argv[1])
    spin = sys.argv[2]
    global order
    if spin == 'cw':
        order = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    elif spin == 'ccw':
        order = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    else:
        print("Bad spin, needs to be `cw` or `ccw`.")
        sys.exit()
    spiral(n)