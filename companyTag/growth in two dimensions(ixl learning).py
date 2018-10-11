#
# Complete the 'countMax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING_ARRAY upRight as parameter.
#

def countMax(upRight):
    # Write your code here
    if not upRight:
        return 0
    minCol = 2 ** 32 - 1
    minRow = 2 ** 32 - 1
    for string in upRight:
        row,col = string.split(' ')
        minCol = min(int(col),minCol)
        minRow = min(int(row),minRow)
    return minCol * minRow