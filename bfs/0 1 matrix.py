import queue


class Solution(object):

    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix

        height = len(matrix)
        weight = len(matrix[0])

        ret = [[0 for _ in range(weight)] for _ in range(height)]

        for i in range(height):
            for j in range(weight):
                ret[i][j] = self.findNearestZero(matrix, i, j)

        return ret

    def findNearestZero(self, matrix, i, j):
        if matrix[i][j] == 0:
            return 0

        diffX = (1,0,-1,0)
        diffY = (0,1,0,-1)

        q = queue.Queue()
        dis = 1
        q.put((i, j))
        while not q.empty():
            l = q.qsize()
            for j in range(l):
                curr = q.get()
                for i in range(len(diffX)):
                    if self.inPosition(matrix, curr[0]+diffX[i], curr[1]+diffY[i]):
                        if matrix[curr[0]+diffX[i]][curr[1]+diffY[i]] == 1:
                            q.put((curr[0]+diffX[i], curr[1]+diffY[i]))
                        else:
                            return dis
            dis += 1
        return dis

    def inPosition(self, matrix, i, j):
        height = len(matrix)
        weight = len(matrix[0])

        if 0 <= i < height and 0 <= j < weight:
            return True
        return False
