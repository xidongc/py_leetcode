import heapq


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        hashmap = {1}
        h = [1]
        heapq.heapify(h)

        for i in range(n-1):
            m = heapq.heappop(h)
            for x in [2*m, 3*m, 5*m]:
                if x not in hashmap:
                    hashmap.add(x)
                    heapq.heappush(h, x)
        return heapq.heappop(h)

s = Solution()
print(s.nthUglyNumber(10))
