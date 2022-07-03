def mid(toCheck):
    if len(toCheck) % 2 == 0:
        return ""
    else:
        midLen = int(len(toCheck)/2)
        midLetter = toCheck[midLen]
        return midLetter