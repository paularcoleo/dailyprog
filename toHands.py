# 280 0 to 100, Real Quick
# https://www.reddit.com/r/dailyprogrammer/comments/4z04vj/20160822_challenge_280_easy_0_to_100_real_quick/

inputs = [[0,1,1,1,0,1,1,1,0,0], [1,0,1,0,0,1,0,0,0,0], [0,0,1,1,1,0,1,1,1,0], [0,0,0,0,1,1,0,0,0,0], [1,1,1,1,1,1,0,0,0,1]]

def decodeHand(hand, left=False):
    count = 0
    for i, digit in enumerate(hand):
        if not (i == 0 or i == 1) and (hand[i] > hand[i-1]):
            return None 
        count += 5*digit if i == 0 else digit
    count *= 10 if left else 1
    return count


for inp in inputs:
    right = inp[5:]
    left = list(reversed(inp[:5]))
    leftcount = decodeHand(left, True)
    rightcount = decodeHand(right)
    if leftcount is None or rightcount is None:
        print("Invalid")
    else:
        print(leftcount + rightcount)
