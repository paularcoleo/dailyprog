# #276 [Easy] REKTangles
# https://www.reddit.com/r/dailyprogrammer/comments/4tetif/20160718_challenge_276_easy_recktangles/

def get_rektangle(phrase, width, height):
    start, end, filler  = phrase[0], phrase[-1], phrase[1:-1]
    rektangle = []
    for i in range(0, height+1):
        thisline = ""
        for j in range(0, width+1):
            letter = start if (i + j) % 2 == 0  else end
            if j == width:
                myfiller = ""
            else:
                myfiller = filler if (i + j) % 2 == 0  else filler[::-1]
            thisline += letter + myfiller
        rektangle.append(thisline)
        # add the columns
        for k in range(0, len(filler)):
            if i == height:
                continue
            column_filler = ""
            for q in range(0, width+1):
                extra = ""
                new = filler[k] if q % 2 == 0 ^ i % 2 ==0 else filler[-k - 1]
                if not q == width:
                    for x in range(0, len(filler)):
                        extra += " "
                column_filler += new + extra
            rektangle.append(column_filler)
    return rektangle

rekt = get_rektangle("REKT",4,3)
for line in rekt:
    print(line)
