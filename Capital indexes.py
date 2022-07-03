#my solution
def capital_indexes(toCheck):
    outList = []
    splitList = list(toCheck)
    lenList = len(toCheck)
    indexNum = 0
    for x in splitList:
        if x.isupper():
            outList.append((indexNum))
        indexNum += 1
    return outList
#example solution
#from string import uppercase
#def capital_indexes(s):
#    return [i for i in range(len(s)) if s[i] in uppercase]