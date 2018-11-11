# v1 by mengfei
# not a good solution by xidong

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


# v2 by mengfei
# good solution using hash O(n) by xidong

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)  # remove duplicate
        maxv = 0
        while nums:
            x = nums.pop()
            before, after = x - 1, x + 1
            length = 1
            while before in nums:
                nums.remove(before)
                before -= 1
                length += 1
            while after in nums:
                nums.remove(after)
                after += 1
                length += 1
            maxv = max(maxv, length)

        return maxv

# v3 by xidong O(nlgn) two pinters


class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <= 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        nums.append(-1)
        print(nums)
        max_num = 1
        p1 = 0
        p2 = 1
        while p2 <= len(nums) - 1:
            if nums[p2] == nums[p2-1]+1:
                p2 += 1
            else:
                max_num = max(max_num, p2 - p1)
                p1 = p2
                p2 += 1
        return max_num






