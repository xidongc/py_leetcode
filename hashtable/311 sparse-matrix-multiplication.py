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
        res = [[0 for _ in range(bCol)] for _ in range(aRow)]
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


# hashmap Solution O(n**2)
class Solution(object):

    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        # corner case
        if len(A) == 0 or len(B) == 0 or len(A[0]) != len(B):
            return -1  # error

        m = len(A)
        n = len(B[0])

        output = [[0 for _ in range(n)] for _ in range(m)]

        hashmap = dict()

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    tmp = hashmap.get(j, list())
                    tmp.append((i, A[i][j]))
                    hashmap[j] = tmp

        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j] != 0:
                    if i in hashmap:
                        for ele in hashmap[i]:
                            output[ele[0]][j] += ele[1] * B[i][j]

        return output


# brute force solution AC
class Solution(object):

    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A) == 0 or len(A[0]) == 0 or len(B) == 0 or len(B[0]) == 0:
            return False
        if len(A[0]) != len(B):
            return False

        matrix = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

        for x in range(len(A)):
            for y in range(len(B[0])):
                value = 0
                for z in range(len(B)):
                    value += A[x][z] * B[z][y]
                matrix[x][y] = value

        return matrix