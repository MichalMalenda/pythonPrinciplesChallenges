#my solution
def all_equal(toCheck):
    splitList = list(toCheck)
    for x in range(len(splitList)):
        if splitList[x] != splitList[0]:
            return False
    return True
#example solution
#def all_equal(items):
#    return all(item1 == item2 for item1 in items for item2 in items)