class Solution(object):

    def __init__(self):
        self.sol = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        rets = []
        sols = self.cal(n)
        for sol in sols:
            ret = []
            for i in range(n):
                ret.append("."*(sol[i]-1)+"Q"+"."*(n-sol[i]))
            rets.append(ret)
        return rets

    def cal(self, n):
        curr = []
        if n <= 0:
            return self.sol

        self.DFS(n, curr, 1)
        return self.sol

    def DFS(self, n, curr, l):
        if len(curr) == n:
            print(curr)
            self.sol.append(curr[:])

        elif len(curr) > n:
            return

        else:
            tmp = [curr[j] + l - 1 - j for j in range(len(curr))
                   if 1 <= (curr[j] + l - 1 - j) <= n]
            tmp_2 = [curr[j] - l + 1 + j for j in range(len(curr))
                     if 1 <= (curr[j] - l + 1 + j) <= n]
            tmp.extend(tmp_2)
            tmp.extend(curr)

            for i in range(1, n+1):
                if i not in tmp:  # need to add \/
                    curr.append(i)
                    self.DFS(n, curr, l+1)
                    curr.pop()


s = Solution()
s.solveNQueens(8)