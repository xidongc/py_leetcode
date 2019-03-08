class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A:
            return [[]]
        aRow = len(A)
        aCol = len(A[0])
        bCol = len(B[0])
        res = [[0 for i in range(bCol)] for j in range(aRow)]
        bMap = {}
        for row in range(aCol):
            bMap[row] = {}
            for col in range(bCol):
                if B[row][col]:
                    bMap[row][col] = B[row][col]
        for arow in range(aRow):
            for acol in range(aCol):
                if A[arow][acol]:
                    for bcol in  bMap[acol]:
                        res[arow][bcol] += A[arow][acol] * bMap[acol][bcol]
        return res