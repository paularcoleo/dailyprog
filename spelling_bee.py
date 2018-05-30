import sys

def main(letters, length):
    central_letter = letters[0]
    with open('words.txt', 'r') as fh:
        words = fh.read().splitlines()
	answers = [w for w in words if "'" not in w and central_letter in w and len(w) >= length and len(set(w) - set(letters)) == 0]
	print('\nANSWERS\n=======================')
    for answer in answers:
        extra = '*' if set(answer) == set(letters) else ''
        print(answer+extra)


if __name__ == '__main__':
    letters = sys.argv[1]
    try:
		length = int(sys.argv[2])
    except IndexError:
        length = 5
    print(sys.argv)
    main(letters, length)
