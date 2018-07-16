class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.fa = [i for i in range(len(M))]
        for i in range(len(M)):
            for j in range(i+1, len(M[i])):
                if M[i][j] == 1:
                    self.Union(i, j)
        fa_cnt = set()
        for i in range(len(M)):
            fa_cnt.add(self.Find(i))
        return len(fa_cnt)

    def Union(self, x, y):
        fx, fy = self.Find(x), self.Find(y)
        if fx != fy:
            self.fa[fx] = fy

    def Find(self, x):
        p = x
        while p != self.fa[p]:
            p = self.fa[p]
        while x != self.fa[x]:
            t = self.fa[x]
            self.fa[x] = p
            x = t
        return p

