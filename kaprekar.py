# #287 [Easy] Kaprekar's Routine
# https://www.reddit.com/r/dailyprogrammer/comments/56tbds/20161010_challenge_287_easy_kaprekars_routine/


def largest_digit(n):
    return int(max(str(n)))


def desc_digits(n, std=True):
    n = "0" * (4 - len(str(n))) + str(n)
    return int(('').join(sorted(str(n), reverse=std)))


def kaprekar(n, iters=0):
    if n in [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]:
        return 0
    if n == 6174:
        return iters
    kap = desc_digits(n) - desc_digits(n, False)
    return kaprekar(kap, iters=iters + 1)


kap_dict = {}


def largest_kap():
    for num in range(1000, 10000):
        kap_dict[num] = kaprekar(num, iters=0)
    return max(kap_dict.values())


if __name__ == "__main__":
    assert largest_digit(1234) == 4
    assert largest_digit(3253) == 5
    assert largest_digit(9800) == 9
    assert largest_digit(3333) == 3
    assert largest_digit(120) == 2
    print("All Standard passed")

    assert desc_digits(1234) == 4321
    assert desc_digits(3253) == 5332
    assert desc_digits(9800) == 9800
    assert desc_digits(3333) == 3333
    assert desc_digits(120) == 2100
    print("All Bonus 1 passed")

    assert kaprekar(6589) == 2
    assert kaprekar(5455) == 5
    assert kaprekar(6174) == 0
    print("All Bonus 2 passed")

    print("Largest # of iterations is: ", largest_kap())
