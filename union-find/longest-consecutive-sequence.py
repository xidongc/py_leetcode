class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))  # remove duplicate
        self.fa = {k: k for k in nums}
        for x in nums:
            if (x - 1) in self.fa:
                self.Union(x, x - 1)
        fa_cnt = dict()
        maxv = 0
        for x in nums:
            fx = self.Find(x)
            if fx not in fa_cnt:
                fa_cnt[fx] = 1
            else:
                fa_cnt[fx] += 1
            maxv = max(maxv, fa_cnt[fx])
        return maxv
        

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
