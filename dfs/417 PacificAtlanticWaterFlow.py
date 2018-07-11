class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        if not matrix:
            return res
        row = len(matrix)
        col = len(matrix[0])
        self.directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        pVisited = [[False for i in range(col)] for j in range(row)]
        aVisited = [[False for i in range(col)] for j in range(row)]
        for i in range(row):
            self.dfs(matrix, i, 0, pVisited)
            self.dfs(matrix, i, col - 1, aVisited)

        for j in range(col):
            self.dfs(matrix, 0, j, pVisited)
            self.dfs(matrix, row - 1, j, aVisited)

        for i in range(row):
            for j in range(col):
                if aVisited[i][j] and pVisited[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, matrix, i, j, visited):
        visited[i][j] = True
        for direction in self.directions:
            curRow = i + direction[0]
            curCol = j + direction[1]
            if curRow < 0 or curRow >= len(matrix) or curCol < 0 or curCol >= len(matrix[0]) or visited[curRow][
                curCol] or matrix[curRow][curCol] < matrix[i][j]:
                continue
            self.dfs(matrix, curRow, curCol, visited)

# 用两个[[]]来表示走得到a和走得到p。因为边界的所有点都是起码可以到达一个p或者a的，故遍历不用两个for遍历所有点，而是从
# 边界往里走遍历。同时把方向存成[[1, 0], [0, 1], [-1, 0], [0, -1]]， 这样就不用四个方向写四次了。只有符合要求的
# 点才会进入下一次dfs遍历，故dfs开始设置为true