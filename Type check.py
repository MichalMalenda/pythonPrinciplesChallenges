#my solution
def only_ints(var1, var2):
    try:
        var1 = int(str(var1))
    except:
        var1 = "a"
    try:
        var2 = int(str(var2))
    except:
        var2 = "a"
    if isinstance(var1, int) == True and isinstance(var2, int) == True:
        return True
    else:
        return False
#example solution
#def only_ints(a, b):
#    return type(a) == int and type(b) == int