# https://www.reddit.com/r/dailyprogrammer/comments/4savyr/20160711_challenge_275_easy_splurthian_chemistry/

inputs = {
    # 'Spenglerium': 'Ee',
    # 'Zuulon': 'Zu',
    'Xenon': 'Xn'
    # 'Zeddemorium': 'Zr',
    # 'Venkmine': 'Kn',
    # 'Stantzon': 'Zt',
    # 'Melintzum': 'Nn',
    # 'Tullium': 'Ty',
    # 'Garbo': 'Zz'
}

def check_Symbol(element, symbol):
    element_chars = list(element.lower())
    first, second = list(symbol.lower())
    first_indices = [i for i, x in enumerate(element_chars) if x == first]
    if len(first_indices) > 0:
        for i in range(0,len(first_indices)):
            second_indices = [i for i, x in enumerate(element_chars[first_indices[i]+1:]) if x == second]
            valid = True if len(second_indices) > 0 else False
            if valid: return valid
    return False


def currentIsLower(current, lowest):
    return True if ord(current) < ord(lowest) else False

def getAlphabetical(element):
    element_chars = list(element.lower())
    first = 'z'
    second = 'z'
    split_index = None
    for index, char in enumerate(element_chars):
        if currentIsLower(char, first):
            first = char
            split_index = index

    for char2 in element_chars[split_index+1:]:
        if currentIsLower(char2, second):
            second = char2

    return first.upper() + second

# close, but doesn't allow for names with the same letter twice -> need ot be able to find number of unique repeats
def getNumOptions(element):
    element_norepeat = ''.join(sorted(set(element), key=element.index)).lower()
    unique_repeats = list(set(filter(lambda x: element.count(x.lower()) > 1, element)))
    return sum(range(1, len(element_norepeat))) + len(unique_repeats)


# def findUniqueCombos(element, num, total=0, used = []):
#     if len(element) == num:
#         return 1
#     if num == 1:
#         used.append(element.lower()[0])
#         print(element, used, " --> " + str(len(''.join(set(element[1:])))))
#         return len(''.join(set(element)))
#     for i in range(0, len(element)):
#         if element.lower()[i] in used:
#             continue
#         total += findUniqueCombos(element[i:],num-1, total, used)
#     return total

# def findUniqueCombos(element, num, depth=0, used =[], total=0):
#     print(element, "\tdepth is: " + str(depth), "combo num is: " + str(num))
#     if len(element) < num:
#         return 0
#     if num == 1:
#         used.append(element[0])
#         print("\tin this recursion I found: " + str(len(''.join(set(element[1:])))) + " new combos\n")
#         return len(''.join(set(element[1:])))
#     for i in range(0, len(element)):
#         used = []
#         if element[i] in used:
#             continue
#         total += findUniqueCombos(element[i+1:],num-1, depth+1, used, total)
#     return total

def findNumUniqueCombos(element, num, used=[], this = 0):
    print(element, num, used)
    if len(element) < num:
        return 0
    if num == 1:
        used.append(element[0])
        return len(''.join(set(element[1:])))
    this += findNumUniqueCombos(element[1:], num-1, used)
    used = []
    return this




for element, symbol in inputs.items():
    # print("Default:  " + element + ", " +\
    #       symbol + " -> " + str(check_Symbol(element, symbol)))
    # print("Bonus 01: " + element + " -> " + getAlphabetical(element))
    # print("Bonus 02: " + element + " -> " + str(getNumOptions(element)))
    # print('')
    element = element.lower()
    total = 0
    for i in range(1,len(element)+1):
        total += findNumUniqueCombos(element, i)
    print(total)
