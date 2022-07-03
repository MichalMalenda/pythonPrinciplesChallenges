#my solution
def add_dots(toCheck):
    splitList = list(toCheck)
    for x in range(len(splitList)):
        if x != len(splitList) - 1:
            splitList[x] = str(splitList[x] + ".")
    outList = ''.join(map(str, splitList))
    return outList


def remove_dots(toCheck):
    return toCheck.replace(".", "")

#example solution
#def add_dots(s):
#    return ".".join(s)
#
#def remove_dots(s):
#    return s.replace(".", "")