# czgg
class Solution(object):

    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp_array = [1]*2  # space optimization
        max_len = 1

        for i, num in enumerate(nums[1:]):
            i += 1
            if num > nums[i-1]:
                dp_array[i % 2] = dp_array[(i-1) % 2] + 1
                max_len = max(max_len, dp_array[i % 2])
            else:
                dp_array[i % 2] = 1

        return max_len

# dup-rabbit
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        res = 0
        cnt = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                cnt += 1
                res = max(cnt,res)
            else:
                cnt = 1
        return res


# mao mao
class Solution(object):

    def findLengthOfLCIS(self, nums) -> int:

        # corner case
        if len(nums) == 0:
            return 0

        i = 1
        gl_count = 1
        while i < len(nums):
            count = 1
            while i < len(nums) and nums[i] > nums[i - 1]:
                count += 1
                i += 1
            gl_count = max(gl_count, count)
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            while i < len(nums) and nums[i] < nums[i - 1]:
                i += 1
        return gl_count
