# #286 Zeckendorf Representations of Positive Integers
# https://www.reddit.com/r/dailyprogrammer/comments/55zdxx/20161005_challenge_286_intermediate_zeckendorf/


import math
from itertools import combinations
Phi = (5 ** 0.5 + 1) / 2
phi = 1 / Phi


def get_next_lowest_fib(n, i=2):
    while i <= n:
        yield round((Phi ** i - ((-1 * phi) ** i)) / (5 ** 0.5))
        i += 1


def zeckendorf(n):
    fib_index = round((math.log(n) + math.log(5) / 2) / (math.log(Phi)))
    fibs = [i for i in get_next_lowest_fib(fib_index)]
    possibles = []
    for i in range(1, len(fibs) + 1):
        for combo in combinations(fibs, i):
            if sum(combo) == n:
                possibles.append(combo)

    for pcombo in possibles:
        for num in pcombo:
            num_index = fibs.index(num)
            if num_index + 1 < len(fibs):
                next_num = fibs[num_index + 1]
                if next_num in pcombo:
                    break
        else:
            return set(pcombo)


print([(i, zeckendorf(i)) for i in [120, 34, 88, 90, 320]])


if __name__ == "__main__":
    assert [zeckendorf(i) for i in [4, 100, 30]] == \
        [{1, 3}, {89, 8, 3}, {21, 8, 1}]
    print("All passed.")
