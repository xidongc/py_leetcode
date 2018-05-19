class Solution:
    def __init__(self):
        self.ret = []

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

s = Solution()
print(s.combine(4, 2))