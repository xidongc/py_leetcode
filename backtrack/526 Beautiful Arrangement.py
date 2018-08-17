import copy
class Solution(object):
    def countArrangement(self,N):
        """
        :type N: int
        :rtype: int
        """
        Solution.res = 0
        visited = [0 for _ in range(N+1)]
        def backtrack(N,visited,pos):
            if pos > N:
                Solution.res += 1
                return
            #  记得什么时候要start什么时候不用start
            for i in range(1, N + 1):
                if visited[i] == 0 and (i % pos == 0 or pos % i == 0):
                    visited[i] = 1
                    backtrack(N,visited,pos + 1)
                    visited[i] = 0
        backtrack(N,visited,1)
        return Solution.res
s = Solution()
print(s.countArrangement(2))