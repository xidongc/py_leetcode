import queue


class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_island = 0

        if not grid or len(grid) == 0:
            return num_island

        h = len(grid)
        w = len(grid[0])

        bool_matrix = [[False for _ in range(w)] for _ in range(h)]

        q = queue.Queue()

        for i in range(h):
            for j in range(w):
                if bool_matrix[i][j] is False and int(grid[i][j]) == 1:
                    # bfs
                    num_island += 1
                    q.put((i, j))
                    bool_matrix[i][j] = True

                    while not q.empty():
                        (num_i, num_j) = q.get()
                        if num_j < w-1:
                            if not bool_matrix[num_i][num_j+1] and int(grid[num_i][num_j+1]) == 1:
                                bool_matrix[num_i][num_j+1] = True
                                q.put((num_i, num_j+1))

                        if num_i < h-1:
                            if not bool_matrix[num_i+1][num_j] and int(grid[num_i+1][num_j]) == 1:
                                bool_matrix[num_i+1][num_j] = True
                                q.put((num_i+1, num_j))

                        if num_j >=1:
                            if not bool_matrix[num_i][num_j-1] and int(grid[num_i][num_j-1]) == 1:
                                bool_matrix[num_i][num_j-1] = True
                                q.put((num_i, num_j-1))

                        if num_i >=1:
                            if not bool_matrix[num_i-1][num_j] and int(grid[num_i-1][num_j]) == 1:
                                bool_matrix[num_i-1][num_j] = True
                                q.put((num_i-1, num_j))

        return num_island

s = Solution()
result = s.numIslands([["1","1","1"],["0","1","1"],["1","1","0"]])
print(result)