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
