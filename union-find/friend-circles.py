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

# by xidong


class Solution(object):

    def __init__(self):
        self.father = dict()

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.father = {i: i for i in range(len(M))}
        ans = set()

        if len(M) <= 0 or len(M[0]) <= 0:
            return 0

        for i in range(len(M)):
            for j in range(i+1, len(M[i])):
                if M[i][j]:
                    self.union(i, j)

        for i in range(len(M)):
            ans.add(self.find(i))

        return len(ans)

    def find(self, x):
        if x == self.father[x]:
            return x

        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, x1, x2):
        root_1 = self.find(x1)
        root_2 = self.find(x2)
        if root_1 != root_2:
            self.father[root_1] = root_2
