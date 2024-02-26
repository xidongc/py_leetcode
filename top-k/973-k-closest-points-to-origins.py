import heapq
import math


class Solution(object):

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        h = list()
        heapq.heapify(h)
        result = list()

        for point in points:
            dis = math.pow(point[0], 2) + math.pow(point[1], 2)
            heapq.heappush(h, (dis, point))

        tmp = K
        while tmp > 0:
            result.append(heapq.heappop(h)[1])
            tmp -= 1
        return result
