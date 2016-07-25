# #277 Simplifying Fractions
# https://www.reddit.com/r/dailyprogrammer/comments/4uhqdb/20160725_challenge_277_easy_simplifying_fractions/

inputs = [(4,8), (1536,78360), (51478, 5536), (46410, 119340), (7673, 4729), (4096, 1024)]

def findFirstDivisor(number):
    for i in range(2, number):
        if number % i == 0:
            return i
    return number

def tree(number):
    fact_tree = {}
    while findFirstDivisor(number):
        div = findFirstDivisor(number)
        fact_tree[div] = 1 if div not in fact_tree.keys() else fact_tree[div] + 1
        number = int(number / div)
        if number == 1:
            return fact_tree

def recombine(num_tree, dem_tree):
    num, dem = 1, 1
    for key, value in num_tree.items():
        num *= key ** value
    for key, value in dem_tree.items():
        dem *= key ** value
    return [num, dem]

def simplify(inputset):
    num_tree = tree(inputset[0])
    dem_tree = tree(inputset[1])

    for key in num_tree.keys():
        if key in dem_tree.keys():
            num_amount, dem_amount = num_tree[key], dem_tree[key]
            num_tree[key] = num_amount-dem_amount if num_amount>dem_amount else 0
            dem_tree[key] = dem_amount-num_amount if dem_amount>num_amount else 0

    return recombine(num_tree, dem_tree)


for inputset in inputs:
    print(simplify(inputset))