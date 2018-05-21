class Solution(object):
    def __init__(self):
        self.ret = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 0:
            return self.ret

        marked = [False for _ in range(len(nums))]
        curr = []
        self.back_tracking(curr, nums, marked)
        return self.ret

    def back_tracking(self, curr, nums, marked):
        if len(curr) == len(nums):
            self.ret.append(curr[:])
            return
        elif len(curr) > len(nums):
            return
        for i, num in enumerate(nums):
            if marked[i] is False:
                marked[i] = True
                curr.append(num)
                self.back_tracking(curr, nums, marked)
                marked[i] = False
                curr.pop()

s = Solution()
nums = [1,2,3]
print(s.permute(nums))

