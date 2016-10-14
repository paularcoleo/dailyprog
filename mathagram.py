# #287 [Intermediate] Mathagrams
# https://www.reddit.com/r/dailyprogrammer/comments/576o8o/20161012_challenge_287_intermediate_mathagrams/

import re
from collections import Counter
from itertools import permutations
from mg_inputs import test_inputs

split_up = lambda x: re.split(' \+ | = ', x)


def missing_nos(numstrs, n):
    present = [int(x) for x in ''.join(numstrs) if x != 'x']
    present_count = Counter(present)
    answer_count = Counter(list(range(1, 10)) * n)
    missing_count = answer_count - present_count
    missing_flat = [[k] * v for k, v in missing_count.items()]
    return [item for sublist in missing_flat for item in sublist]


def evaluate_mathagram(inputs, n):
    rhs, lhs = inputs[:-n], inputs[-n:]
    rh_sum, lh_sum = sum(int(x) for x in rhs), sum(int(y) for y in lhs)
    if rh_sum == lh_sum:
        return True
    return False


def fill_in_gram(inputstr, missing):
    # inputs should be given as raw input_string
    m_index = 0
    filled_str = ''
    for char in inputstr:
        if char == 'x':
            filled_str += str(missing[m_index])
            m_index += 1
        else:
            filled_str += char
    return split_up(filled_str)


def brute_force(inputs, n):
    missing = missing_nos(split_up(inputs), n)
    perms = permutations(missing)
    for perm in perms:
        test_gram = fill_in_gram(inputs, perm)
        if evaluate_mathagram(test_gram, n):
            return test_gram


for challenge, n in test_inputs:
    print(brute_force(challenge, n))
