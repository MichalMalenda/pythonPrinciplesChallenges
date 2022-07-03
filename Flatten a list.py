#my solution, without numpy
def flatten(toCheck):
    from itertools import chain
    return list(chain.from_iterable(toCheck))
#my solution with numpy
def flatten(toCheck):
    from numpy import array
    x = array(toCheck)
    return list(x.flat)
#example solution
#def flatten(outer_list):
#    return [
#        item
#        for inner_list in outer_list
#        for item in inner_list
#    ]