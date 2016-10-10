# #275[Easy] Splurthian Chemistry 101
# https://www.reddit.com/r/dailyprogrammer/comments/4savyr/20160711_challenge_275_easy_splurthian_chemistry/

inputs = {
    'Spenglerium': 'Ee',
    'Zuulon': 'Zu',
    'Zeddemorium': 'Zr',
    'Venkmine': 'Kn',
    'Stantzon': 'Zt',
    'Melintzum': 'Nn',
    'Tullium': 'Ty',
    'Garbo': 'Zz'
}


def check_Symbol(element, symbol):
    element_chars = list(element.lower())
    first, second = list(symbol.lower())
    first_indices = [i for i, x in enumerate(element_chars) if x == first]
    if len(first_indices) > 0:
        for i in range(0, len(first_indices)):
            second_indices = [
                i for i, x in enumerate(element_chars[first_indices[i] + 1:])
                if x == second]

            valid = True if len(second_indices) > 0 else False
            if valid:
                return valid
    return False


for element, symbol in inputs.items():
    print("Default:  " + element + ", " +
          symbol + " -> " + str(check_Symbol(element, symbol)))
