class Solution:
    def __init__(self):
        self.ret = []
#1
    def combine(self, n, k):
        curr = []
        if n <= 0:
            return self.ret

        self.DFS(curr, n, k, 1)
        return self.ret

    def DFS(self, curr, n, k, level):
        if len(curr) == k:
            print(curr)
            self.ret.append(curr[:])
            return

        elif len(curr) > k:
            return

        for i in range(level, n+1):
            curr.append(i)
            self.DFS(curr, n, k, i+1)
            curr.pop()
#2
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        Solution.res = []
        self.helper(n,1,k,[])
        return Solution.res
    def helper(self,n,start,k,tempList):
        if len(tempList) == k:
            Solution.res.append(tempList)
            return
        for i in range(start,n+1):
            self.helper(n,i+1,k,tempList+[i])
s = Solution()
print(s.combine(4, 2))
