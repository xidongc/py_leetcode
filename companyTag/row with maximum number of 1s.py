# from geeks for geeks

# Python3 program to find the row
# with maximum number of 1s

# Function to find the index
# of first index of 1 in a
# boolean array arr[]

def rowWithMax1s(matrix):
    index = 0
    j = first(matrix) # find most left 1 for row 0
    if j == -1:
        j = len(matrix[0]) - 1

    for i in range(1, len(matrix)):
        while j >= 0 and matrix[i][j] == 1:
            j -= 1
            index = i
    return index