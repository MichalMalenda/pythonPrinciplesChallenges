#my solution
def get_row_col(toCheck):
    board = [
        ["X", "O", "X"],
        [" ", " ", " "],
        ["O", " ", " "],
    ]
    splitList = list(board)
    splitList2 = list(toCheck)
    if splitList2[0] == "A":
        splitList2[0] = 0
    elif splitList2[0] == "B":
        splitList2[0] = 1
    elif splitList2[0] == "C":
        splitList2[0] = 2
    if splitList2[1] == "1":
        splitList2[1] = 0
    elif splitList2[1] == "2":
        splitList2[1] = 1
    elif splitList2[1] == "3":
        splitList2[1] = 2
    temp1 = splitList2[0]
    temp2 = splitList2[1]
    out = (temp2, temp1)
    return out
#example solution
#def get_row_col(choice):
#    translate = {"A": 0, "B": 1, "C": 2}
#    letter = choice[0]
#    number = choice[1]
#    row = int(number) - 1
#    column = translate[letter]
#    return (row, column)