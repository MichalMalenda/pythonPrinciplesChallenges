#my solution
def consecutive_zeros(toCheck):
    splitList = list(toCheck)
    temp1 = 0
    temp2 = 0
    for x in range(len(splitList)):
        if splitList[x] == "0":
            temp1 += 1
        elif splitList[x] == "1":
            if temp2 < temp1:
                temp2 = temp1
            temp1 = 0
    if temp2 < temp1:
        temp2 = temp1
    return temp2
#example solution
#def consecutive_zeros(bin_str):
#    return max([len(s) for s in bin_str.split("1")])