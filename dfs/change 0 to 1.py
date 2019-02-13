# 是在一个image（2d array）上选择一个点，然后遇到0就把0变成1，遇到1就停止，
# 比较简单的一个DFS吧，然而第一次写的时候下意思地写了一个visited来存访问过的点，
# 面试官提醒了一下可以直接修改原array，就去掉了
dirs =[[0,1],[1,0],[-1,0],[0,-1]]
def change(matrix):
    dfs(matrix,2,2)

def dfs(matrix,row,col):
    matrix[row][col] = 1
    for dir in dirs:
        x = row + dir[0]
        y = col  + dir[1]
        if x >= 0 and y >= 0 and x < len(matrix) and y < len(matrix[0]) and matrix[x][y] == 0:
            dfs(matrix,x,y)
matrix =[[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
change(matrix)
print(matrix)