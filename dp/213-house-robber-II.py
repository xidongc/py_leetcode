class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            return max(self.rob_I(nums[1:]), self.rob_I(nums[0:-1]))

    def rob_I(self, nums):
        dp_array = [0] * 3

        dp_array[0] = nums[0]
        dp_array[1] = max(nums[0], nums[1])

        i = 1

        for i, num in enumerate(nums[2:]):
            i += 2
            dp_array[i % 3] = max(dp_array[(i-1) % 3], dp_array[(i-2) % 3]+num)

        return dp_array[i % 3]

s = Solution()
s.rob([1,2,3,1])
