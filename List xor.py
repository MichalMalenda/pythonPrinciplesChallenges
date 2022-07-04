#my solution
def list_xor(n, var1, var2):
    if n in var1 and n in var2:
        return False
    elif n not in var1 and n not in var2:
        return False
    else:
        return True
#example solution
#def list_xor(n, list1, list2):
#    return (n in list1) ^ (n in list2)