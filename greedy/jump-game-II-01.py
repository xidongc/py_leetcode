class Solution(object):

    def __init__(self):
        self.count = float("inf")

    def jump(self, nums):
        if len(nums) <= 1:
            return 0

        """
        :type nums: List[int]
        :rtype: int
        """
        curr = []
        self.dfs(curr, 0, nums[0], nums)
        return self.count

    def dfs(self, curr, index, step, nums):
        if index + step >= len(nums)-1:
            if len(curr) + 1 < self.count:
                self.count = len(curr) + 1
        for j in range(1, step+1):
            if index + j <= len(nums) -1:
                curr.append(index)
                max_step = max(nums[index+j], step-j)
                self.dfs(curr, index+j, max_step, nums)
                curr.pop()
s = Solution()
nums = [6,2,6,1,7,9,3,5,3,7,2,8,9,4,7,7,2,2,8,4,6,6,1,3]
print(s.jump(nums))