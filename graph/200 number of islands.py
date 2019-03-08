# bfs solution
class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islandNumber = 0

        # corner case
        if len(grid) == 0 or len(grid[0]) == 0:
            return islandNumber

        queue = list()
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        positions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] is False and grid[i][j] == "1":
                    queue.append((i, j))
                    visited[i][j] = True

                    # bfs
                    while len(queue) > 0:
                        curr = queue.pop(0)
                        for (x, y) in positions:
                            if self.in_position(curr[0] + x, curr[1] + y, len(grid), len(grid[0])) and \
                                    grid[curr[0] + x][curr[1] + y] == "1" and \
                                    visited[curr[0] + x][curr[1] + y] is False:
                                queue.append((curr[0] + x, curr[1] + y))
                                visited[curr[0] + x][curr[1] + y] = True
                    islandNumber += 1
        return islandNumber

    def in_position(self, x, y, rows, cols):
        return 0 <= x < rows and 0 <= y < cols


# union find solution
class UnionFind(object):

    def __init__(self, grid):
        self.count = 0  # count of father
        m = len(grid)
        n = len(grid[0])
        self.father = [-1 for _ in range(m * n)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.father[(i - 1) * n + j] = (i - 1) * n + j
                    self.count += 1

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, x, y):
        father1 = self.find(x)
        father2 = self.find(y)
        if father1 != father2:
            self.father[father1] = father2
            self.count -= 1


class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        uf = UnionFind(grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    for d in directions:
                        x = i + d[0]
                        y = j + d[1]
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
                            uf.union((x - 1) * len(grid[0]) + y, (i - 1) * len(grid[0]) + j)
        return uf.count