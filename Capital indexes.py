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
