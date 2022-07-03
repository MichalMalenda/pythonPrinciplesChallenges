#my solution
def palindrome (toCheck):
    return toCheck == toCheck[::-1]
#example solution
#def palindrome(string):
#    if len(string) < 2:
#        return True
#    return string[0] == string[-1] and palindrome(string[1:-1])