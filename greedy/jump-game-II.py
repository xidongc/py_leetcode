class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        current = next = 0

        i = 0

        while current < len(nums) - 1:
            while i <= current:
                next = max(next, i+nums[i])
                i += 1
            current = next
            next = 0
            step += 1
        return step

s = Solution()
nums = [2,3,1,1,4]
print(s.jump(nums))