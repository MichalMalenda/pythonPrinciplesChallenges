#my solution
def zap(var1, var2):
    result = []
    for x in range(len(var1)):
        result.append((var1[x], var2[x]))
    return result
#example solution
#def zap(a, b):
#    return [(a[i], b[i]) for i in range(len(a))]