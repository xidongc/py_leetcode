class Solution(object):

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix[0]) <= 0:
            return 0
        h = len(matrix)
        w = len(matrix[0])
        dp_arr = [[-1]*w for _ in range(h)]
        max_len = 0

        for i in range(w):
            if matrix[0][i] == "1":
                dp_arr[0][i] = 1
                max_len = 1
            else:
                dp_arr[0][i] = 0

        for i in range(h):
            if matrix[i][0] == "1":
                dp_arr[i][0] = 1
                max_len = 1
            else:
                dp_arr[i][0] = 0

        i = 0

        for i in range(1, h):
            for j in range(1, w):
                if matrix[i][j] == "0":
                    dp_arr[i][j] = 0
                elif matrix[i][j] == "1":
                    if dp_arr[i-1][j-1] == 0 or\
                                    dp_arr[i][j-1] == 0 or\
                                    dp_arr[i-1][j] == 0:
                        dp_arr[i][j] = 1
                    else:
                        dp_arr[i][j] = min(dp_arr[i-1][j-1], dp_arr[i][j-1], dp_arr[i-1][j]) + 1
                    max_len = max(max_len, dp_arr[i][j])

        return max_len * max_len