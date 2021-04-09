import heapq


class Solution(object):

    def kthSmallest(self, matrix: list, k: int) -> int:

        # corner case
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        heap = []
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        mark = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        mark[0][0] = True
        count = 0
        while count < k - 1:
            ele, x, y = heapq.heappop(heap)
            if self.isValid(x + 1, y, len(matrix[0]), len(matrix)) and mark[x + 1][y] is False:
                mark[x + 1][y] = True
                heapq.heappush(heap, (matrix[x + 1][y], x + 1, y))
            if self.isValid(x, y + 1, len(matrix[0]), len(matrix)) and mark[x][y + 1] is False:
                mark[x][y + 1] = True
                heapq.heappush(heap, (matrix[x][y + 1], x, y + 1))
            count += 1
        ele, _, _ = heapq.heappop(heap)
        return ele

    def isValid(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n
