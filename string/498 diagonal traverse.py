# matrix
# (0,0) | (0,1)(1,0) | (2,0)(1,1)(0,2) | (1,2)(2,1)(3,0) | (3,1)(2,2) | (3,2)
#   0         1               2                  3             4          5
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        res = []
        m = len(matrix)
        n = len(matrix[0])
        r,c = 0,0
        while r < m and c < n:
            # goes down
            res.append(matrix[r][c])
            if (c + r) % 2:
                # if hit the leftdown corner, both requirements meet, yet should move right first
                # The sequence of if elif else matters
                if r == m - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
            # goes up
            else:
                # if hit the rightupper corner, both requirements meet, yet should move down first
                if c == n - 1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
        return res
