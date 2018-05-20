class Solution(object):

    def __init__(self):
        self.ret = []

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        curr = []
        self.dfs(curr, k, n, 1)
        return self.ret

    def dfs(self, curr, k, target, l):
        if len(curr) == k and target == 0:
            print(curr) # for debug only
            self.ret.append(curr[:])
            return
        elif len(curr) < k and target > 0:
            for i in range(l, 10):
                curr.append(i)
                self.dfs(curr, k, target-i, i+1)
                curr.pop()
        else:
            return

s = Solution()
print(s.combinationSum3(3, 9))

