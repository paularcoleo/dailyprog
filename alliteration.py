# #288 [Easy] Detecting Alliteration
# https://www.reddit.com/r/dailyprogrammer/comments/57zcbm/20161017_challenge_288_easy_detecting_alliteration/

stopwords = ['i', 'a', 'about', 'an', 'and', 'are', 'as',
             'at', 'be', 'by', 'com', 'for', 'from', 'how',
             'in', 'is', 'it', 'of', 'on', 'or', 'that',
             'the', 'this', 'to', 'was', 'what', 'when',
             'where', 'who', 'will', 'with', 'the']


def extract_alliterations(line):
    valid_words = [(w, w[0].lower()) for w in line.split() if w.lower() not in stopwords]
    allits = []
    s_letter = None
    start, count = 0, 0
    for i, (word, letter) in enumerate(valid_words):
        if i == len(valid_words) - 1 and count >= 2:
            allits.append([x[0] for x in valid_words[start:]])
        if letter == s_letter:
            count += 1
        else:
            if count >= 2:
                allits.append([x[0] for x in valid_words[start:i]])
            start, count = i, 1
            s_letter = letter
    return allits


test_strings_one = [
    "Peter Piper Picked a Peck of Pickled Peppers",
    "Bugs Bunny likes to dance the slow and simple shuffle",
    "You'll never put a better bit of butter on your knife"]

test_strings_two = [
    "The daily diary of the American dream",
    "For the sky and the sea, and the sea and the sky",
    "Three grey geese in a green field grazing, Grey were the geese and green was the grazing.",
    "But a better butter makes a batter better.",
    "His soul swooned slowly as he heard the snow falling faintly through\
        the universe and faintly falling, like the descent of their last \
        end, upon all the living and the dead.",
    "Whisper words of wisdom, let it be.",
    "They paved paradise and put up a parking lot."
    "So what we gonna have, dessert or disaster?"]


for string in test_strings_one:
    solution = extract_alliterations(string)
    print(solution)

for string in test_strings_two:
    solution = extract_alliterations(string)
    print(solution)
