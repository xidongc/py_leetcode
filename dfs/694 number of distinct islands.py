class Solution(object):
    # 1
    def __init__(self):
        self.dirStr = ''
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        islandSet = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dirStr= ''
                    self.helper(grid, i, j, 'o')
                    islandSet.add(self.dirStr)
        return len(islandSet)

    def helper(self, grid, i, j, label):
        #或者用listofstrappend，因为string不可变
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
            return
        self.dirStr += label
        grid[i][j] = 0
        self.helper(grid, i + 1, j, 'u')
        self.helper(grid, i - 1, j, 'd')
        self.helper(grid, i, j + 1, 'l')
        self.helper(grid, i, j - 1, 'r')
        # 层检验
        self.dirStr += 'b'
    # 2
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        islandSet = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    l = []
                    self.helper(grid, i, j, 'o', l)
                    islandSet.add(''.join(l))
        return len(islandSet)

    def helper(self, grid, i, j, label,l):
        #或者用listofstrappend，因为string不可变
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
            return
        # self.dirStr += label
        l.append(label)
        grid[i][j] = 0
        self.helper(grid, i + 1, j, 'u',l)
        self.helper(grid, i - 1, j, 'd',l )
        self.helper(grid, i, j + 1, 'l',l)
        self.helper(grid, i, j - 1, 'r',l)
        # 层检验
        # self.dirStr += 'b'
        l.append('b')
s = Solution()
s.numDistinctIslands([[1,1,0],[0,1,1],[0,0,0],[1,1,1],[0,1,0]])