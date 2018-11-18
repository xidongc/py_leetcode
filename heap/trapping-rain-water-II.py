from queue import PriorityQueue, Queue


class Solution(object):

    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if len(heightMap) <= 2 or len(heightMap[0]) < 1:
            return 0

        q = PriorityQueue()
        h = len(heightMap)
        w = len(heightMap[0])

        mark = [[False for _ in range(w)] for _ in range(h)]

        for i in range(h):
            for j in range(w):
                if i == 0 or i == h-1 or j == 0 or j == w - 1:
                    mark[i][j] = True
                    q.put((heightMap[i][j], i, j))

        sqr = 0
        while not q.empty():
            (curr, i, j) = q.get()
            count = self.bfs(i, j, h, w, heightMap, mark, curr, q)
            sqr += count
        print(sqr)
        return sqr

    def bfs(self, i, j, h, w, heightMap, mark, curr, q):
        count = 0
        neighbors = Queue()
        print(i, j)
        if i == 2 and j == 3:
            print("hello")

        if i > 0 and mark[i-1][j] is False:
            if heightMap[i-1][j] < curr:
                count += (curr - heightMap[i-1][j])
                neighbors.put((heightMap[i-1][j], i-1, j))
            else:
                q.put((heightMap[i-1][j], i-1, j))
            mark[i-1][j] = True

        if i < h-1 and mark[i+1][j] is False:
            if heightMap[i+1][j] < curr:
                count += (curr - heightMap[i+1][j])
                neighbors.put((heightMap[i+1][j], i+1, j))
            else:
                q.put((heightMap[i+1][j], i+1, j))
            mark[i+1][j] = True

        if j < w-1 and mark[i][j+1] is False:
            if heightMap[i][j+1] < curr:
                count += (curr - heightMap[i][j+1])
                neighbors.put((heightMap[i][j+1], i, j+1))
            else:
                q.put((heightMap[i][j+1], i, j+1))
            mark[i][j+1] = True

        if j > 0 and mark[i][j-1] is False:
            if heightMap[i][j-1] < curr:
                count += (curr - heightMap[i][j-1])
                neighbors.put((heightMap[i][j-1], i, j-1))
            else:
                q.put((heightMap[i][j-1], i, j-1))
            mark[i][j-1] = True

        while not neighbors.empty():
            (tmp, i, j) = neighbors.get()

            if i > 0 and mark[i-1][j] is False:
                if heightMap[i-1][j] < curr:
                    count += (curr - heightMap[i-1][j])
                    neighbors.put((heightMap[i-1][j], i-1, j))
                else:
                    q.put((heightMap[i-1][j], i-1, j))
                mark[i-1][j] = True

            if i < h-1 and mark[i+1][j] is False:
                if heightMap[i+1][j] < curr:
                    count += (curr - heightMap[i+1][j])
                    neighbors.put((heightMap[i+1][j], i+1, j))
                else:
                    q.put((heightMap[i+1][j], i+1, j))
                mark[i+1][j] = True

            if j < w-1 and mark[i][j+1] is False:
                if heightMap[i][j+1] < curr:
                    count += (curr - heightMap[i][j+1])
                    neighbors.put((heightMap[i][j+1], i, j+1))
                else:
                    q.put((heightMap[i][j+1], i, j+1))
                mark[i][j+1] = True

            if j > 0 and mark[i][j-1] is False:
                if heightMap[i][j-1] < curr:
                    count += (curr - heightMap[i][j-1])
                    neighbors.put((heightMap[i][j-1], i, j-1))
                else:
                    q.put((heightMap[i][j-1], i, j-1))
                mark[i][j-1] = True
        print(count)

        return count



s = Solution()
heightMap = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
s.trapRainWater(heightMap)





