#my solution
def mid(toCheck):
    if len(toCheck) % 2 == 0:
        return ""
    else:
        midLen = int(len(toCheck)/2)
        midLetter = toCheck[midLen]
        return midLetter
#example solution
#def mid(string):
#    if len(string) % 2 == 0:
#        return ""
#    return string[len(string)//2]