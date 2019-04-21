# Sol-1 brute force AC
class Solution(object):

    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # corner case
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return True

        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if visited[i][j] is False:
                    # check if matches
                    currX, currY = i, j
                    visited[currX][currY] = True
                    while currX + 1 < len(matrix) and currY + 1 < len(matrix[0]):
                        if matrix[currX + 1][currY + 1] == matrix[currX][currY]:
                            visited[currX + 1][currY + 1] = True
                            currX += 1
                            currY += 1
                        else:
                            return False
        return True


# Sol-2 using hashmap (r2-r1 = c2-c1)
class Solution(object):

    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # corner case
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return True

        hashmap = dict()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i - j not in hashmap:
                    hashmap[i - j] = matrix[i][j]
                else:
                    if hashmap[i - j] != matrix[i][j]:
                        return False
        return True
