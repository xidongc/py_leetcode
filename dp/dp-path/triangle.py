# 5 Sols to solve 120-triangle with DP, DFS and Divide Conquer
# Problem link: https://leetcode.com/problems/triangle/description/


# Sol-1: DFS solution, pretty straight forward, LTE
class Solution(object):

    def minimumTotal(self, triangle):

        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        # dfs solution TLE
        # time complexity: O(2^n)

        if not triangle or len(triangle) == 0:
            return 0

        min_path_sum = float("inf")
        curr = []

        def helper(curr, i, j, triangle):
            nonlocal min_path_sum
            if len(curr) == len(triangle):
                min_path_sum = min(min_path_sum, sum(curr))
            if i < len(triangle):
                curr.append(triangle[i][j])
                helper(curr, i+1, j, triangle)
                helper(curr, i+1, j+1, triangle)
                curr.pop()

        helper(curr, 0, 0, triangle)
        print(min_path_sum)
        return min_path_sum


# Sol-2: Divide and Conquer, pretty straight forward, LTE
class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        # divide and conquer
        # time complexity: O(2^n)
        # no time optimization

        def helper(i, j):
            # divide
            if i == len(triangle) - 1:
                return triangle[i][j]

            if i >= len(triangle):
                return

            # conquer
            return min(helper(i+1, j), helper(i+1, j+1)) + triangle[i][j]

        return helper(0, 0)


# Sol-3: Divide Conquer with memorization, LTE
# use hashtable to memorize node which traversed twice in Sol-2
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        # divide and conquer with memorization
        # time complexity O(n^2) with extra space O(n) in hashtable

        hashmap = {}

        def helper(i, j):
            nonlocal hashmap
            # divide
            if i == len(triangle) - 1:
                if hasher(i, j) not in hashmap:
                    hashmap[hasher(i, j)] = triangle[i][j]
                    return triangle[i][j]
                return hashmap[hasher(i, j)]

            if i >= len(triangle):
                return

            # conquer
            if hasher(i+1, j) in hashmap:
                m1 = hashmap[hasher(i+1, j)]
            else:
                m1 = helper(i+1, j)

            if hasher(i+1, j+1) in hashmap:
                m2 = hashmap[hasher(i+1, j+1)]
            else:
                m2 = helper(i+1, j+1)
            return min(m1, m2) + triangle[i][j]

        # given unique id for (i, j)
        def hasher(i, j):
            return int(str(i) + str(j))

        return helper(0, 0)


# Sol-4: DP solution from top -> down with 2d matrix, Accepted
class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # time complexity O(n^2)

        # 2-d dp matrix
        dp = []
        for x in range(len(triangle)):
            dp.append([-1 for _ in range(x+1)])


        # dp from top -> down
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]

                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]

                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

        return min(dp[len(triangle)-1])


# Sol-4 extention with 1d dp (the same approach internally)
class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        height = len(triangle)
        d = [[float("inf") for _ in range(k+1)] for k in range(height)]
        d[0][0] = triangle[0][0]
        dp = [triangle[0][0] for _ in range(height)]
        for i in range(1, height):
            for t in range(i+1):
                if t == 0:
                    d[i][t] = d[i-1][t] + triangle[i][t]
                elif t == i:
                    d[i][t] = d[i-1][t-1] + triangle[i][t]
                else:
                    d[i][t] = min(d[i-1][t-1], d[i-1][t]) + triangle[i][t]
            dp[i] = min(d[i])
        return dp[height-1]


# Sol-5 dp solution with down -> top Accepted
class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # time complexity O(n^2) easier than Sol-4, as no need to consider
        # condition of j == 0 and i == i

        # 2-d dp matrix
        dp = []
        for x in range(len(triangle)):
            dp.append([-1 for _ in range(x+1)])

        # dp from down -> top
        for i in range(len(triangle)-1, -1, -1):
            for j in range(i+1):
                if i == len(triangle)-1:
                    dp[i][j] = triangle[i][j]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]

        return dp[0][0]


# test

s = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(s.minimumTotal(triangle))