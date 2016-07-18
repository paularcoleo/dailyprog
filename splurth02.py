# #275[Intermediate] Splurthian Chemistry 102
# https://www.reddit.com/r/dailyprogrammer/comments/4so25w/20160713_challenge_275_intermediate_splurthian/

eledict = {}

def find_preferred_symbols(element):
    symbols = []
    first, second = '', ''
    for i, char in enumerate(list(element)):
        for char2 in list(element[i+1:]):
            option = char + char2
            if option not in symbols:
                symbols.append(option)
    return symbols


def find_first_available_symbol(symbols, eledict):
    for symbol in symbols:
        if symbol not in eledict.values():
            return symbol
    else:
        return None


with open("splurth02.txt") as fh:
    for line in fh:
        element = line.strip().lower()
        sym = find_first_available_symbol(find_preferred_symbols(element), eledict)
        if sym is not None:
            eledict[element] = sym
        else:
            print("Element: " + element + " cannot be assigned a symbol.")
            break
