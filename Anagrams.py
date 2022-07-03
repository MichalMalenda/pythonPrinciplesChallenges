#my solution
def is_anagram(var1, var2):
    if sorted(var1) == sorted(var2):
        return True
    else:
        return False
#example solution
#def is_anagram(string1, string2):
#    return sorted(string1) == sorted(string2)