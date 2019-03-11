import heapq


class Solution(object):

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        # corner case
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        heap = list()
        heapq.heapify(heap)

        smallestCount = 0

        if smallestCount >= m * n:
            return -1

        for i in range(m):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        while smallestCount < k - 1:
            (ele, ln, li) = heapq.heappop(heap)
            if li < n - 1:
                heapq.heappush(heap, (matrix[ln][li + 1], ln, li + 1))
            smallestCount += 1

        (ele, ln, li) = heapq.heappop(heap)
        return matrix[ln][li]
