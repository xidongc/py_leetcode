class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        res = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(self.bfs(grid,i,j,directions),res)
        return res
    def bfs(self,grid,x,y,directions):
        grid[x][y] = 'X'
        area = 1
        for direction in directions:
            curx = x + direction[0]
            cury = y + direction[1]
            if curx >= 0 and cury >= 0 and curx < len(grid) and cury < len(grid[0]) and grid[curx][cury] == 1:
                area += self.bfs(grid,curx,cury,directions)
        return area
s = Solution()
s.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])