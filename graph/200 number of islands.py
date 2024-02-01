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


# follow up return the distinct island
from collections import deque, defaultdict
class Solution:
    """
    @param grid: the 2D grid
    @return: the number of distinct islands
    """
    def numDistinctIslands2(self, grid):
        # write your code here
        # 1. use BFS to find all islands
        row, col = len(grid), len(grid[0])
        visited = set([])
        delta = [(-1,0),(1,0),(0,1),(0,-1)]
        islands = []
        for r in xrange(row):
            for c in xrange(col):
                min_r, min_c = row, col
                if grid[r][c] == 1 and (r, c) not in visited:
                    min_r, min_c = min(min_r, r), min(min_c, c)
                    visited.add((r, c))
                    island = [[r, c]]
                    dq = deque([ [r, c] ])
                    while dq:
                        curr_r, curr_c = dq.popleft()
                        for dr, dc in delta:
                            new_r, new_c = curr_r + dr, curr_c + dc
                            if not (0 <= new_r <= row - 1 and 0 <= new_c <= col - 1):
                                continue
                            if grid[new_r][new_c] != 1 or (new_r, new_c) in visited:
                                continue
                            visited.add((new_r, new_c))
                            min_r, min_c = min(min_r, new_r), min(min_c, new_c)
                            dq.append([new_r, new_c])
                            island.append([new_r, new_c])
                    # 2. Normalize: shift island to (0,0)
                    for index in xrange(len(island)):
                        island[index][0] -= min_r
                        island[index][1] -= min_c
                    island.sort()
                    islands.append(island)
        # 3. Find representation and count result
        return self.count_unique_islands(islands)
    def count_unique_islands(self, islands):
        s = set([])
        for island in islands:
            s.add(self.find_represent(island))
        return len(s)
    def find_represent(self, island):
        result = []
        result.append(self.convert_island_to_tuple(island))
        result.append(self.convert_island_to_tuple(self.flip(island)))
        rotation = self.rotate(island)
        for _ in xrange(3):
            result.append(self.convert_island_to_tuple(rotation))
            result.append(self.convert_island_to_tuple(self.flip(rotation)))
            rotation = self.rotate(rotation)
        result.sort()
        return result[0]
    def rotate(self, island):
        new_island = []
        max_r, max_c = 0, 0
        for pair in island:
            max_r = max(max_r, pair[0])
            max_c = max(max_c, pair[1])
        for pair in island:
            new_island.append([pair[1], max_r - pair[0]])
        new_island.sort()
        return new_island
    def convert_island_to_tuple(self, island):
        result = []
        for pair in island:
            result.extend(pair)
        return tuple(result)
    def flip(self, island):
        new_island = []
        max_r, max_c = 0, 0
        min_r, min_c = float('inf'), float('inf')
        for r, c in island:
            max_r, max_c = max(max_r, r), max(max_c, c)
            min_r, min_c = min(min_r, r), min(min_c, c)
        for r, c in island:
            new_island.append([r - min_r, max_c - c - min_c])
        new_island.sort()
        return new_island
