#my solution
def double_letters(toCheck):
    splitList = list(toCheck)
    valBol = False
    for x in range(len(splitList)):
        if splitList[x] == splitList[x-1]:
            valBol = True
    return valBol
#example solution
#def double_letters(string):
#    return any([a == b for a, b in zip(string, string[1:])])