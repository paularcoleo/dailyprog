from itertools import combinations, product
from pprint import pprint

tests = ['01234', 'ABCDE', 'FGHI', 'JKL']

def all_pairs(combos):
    copy = combos[:]
    for i, combo in enumerate(combos):
        subcombos = combinations(combo, r=2)
        rest = copy[:i] + copy[i+1:]
        for subcombo in subcombos:
            for test in rest:
                if set(subcombo) <=  set(test):
                    break
            else:
                print('{} is unique for subcomo {}'.format(combo, subcombo))
                break
        else:
            print('{} has no unique subcombos. removing and restarting'.format(combo))
            copy.pop(i)
            return all_pairs(copy)            
    # pprint(copy)
    return copy


initial_combos = list(product(*tests)) 
final_combos = all_pairs(initial_combos)
for c in final_combos:
    print(' '.join(c))
print('exhaustive list: ', len(initial_combos))
print('final list: ', len(final_combos))
print(list([item for item in group] for group in tests))