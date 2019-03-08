class Solution(object):

    def generateMatrix(self, n: int) -> List[List[int]]:

        def helper(ret, startX, startY, level, lastEle):
            if level == 1:
                ret[startX][startY] = lastEle
                return
            if level < 1:
                return

            for i in range(level):
                ret[startX][startY + i] = lastEle + i
            for j in range(level):
                ret[startX + j][startY + i] = lastEle + i + j
            for t in range(level):
                ret[startX + j][startY + i - t] = lastEle + i + j + t
            for h in range(level - 1):
                ret[startX + j - h][startY + i - t] = lastEle + i + j + t + h

            helper(ret, startX + 1, startY + 1, level - 2, lastEle + i + j + t + h + 1)

        ret = [[-1 for _ in range(n)] for _ in range(n)]
        helper(ret, 0, 0, n, 1)
        return ret