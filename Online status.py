def online_count(toCheck):
    returnVal = 0
    for x in range(len(toCheck)):
        if list(toCheck.items())[x][1] == "online":
            returnVal = returnVal + 1
    return returnVal