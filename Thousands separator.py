#my solution
def format_number(toCheck):
    a = ''
    b = 0
    if toCheck > 0:
        toCheck = str(toCheck)
        for item in toCheck[::-1]:
            b += 1
            if b % 3 == 0:
                a = ',' + item + a
            else:
                a = item + a
        if a[0] == ",":
            return str(a[1:])
        else:
            return str(a)
    else:
        return False
#example solution
#def format_number(n):
#    return "{:,}".format(n)