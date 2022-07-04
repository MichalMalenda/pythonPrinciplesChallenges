#my solution
def validate(toCheck):
    if "def validate(toCheck)" in toCheck:
        return True
    elif "def" not in toCheck:
        return "missing def"
    elif ":" not in toCheck:
        return "missing :"
    elif "(" not in toCheck or ")" not in toCheck:
        return "missing paren"
    elif '()' in toCheck or '():' in toCheck or '"()"' in toCheck:
        return "missing param"
    elif "    " not in toCheck:
        return "missing indent"
    elif "validate" not in toCheck:
        return "wrong name"
    elif "return" not in toCheck:
        return "missing return"
    else:
        return True
#example solution
#def validate(code):
#    if "def" not in code:
#        return "missing def"
#    if ":" not in code:
#        return "missing :"
#    if "(" not in code or ")" not in code:
#        return "missing paren"
#    if "(" + ")" in code:
#        return "missing param"
#    if "    " not in code:
#        return "missing indent"
#    if "validate" not in code:
#        return "wrong name"
#    if "return" not in code:
#        return "missing return"
#    return True