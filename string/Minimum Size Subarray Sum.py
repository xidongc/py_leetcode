class Solution(object):

    def minSubArrayLen(self, s: int, nums) -> int:
        if len(nums) == 0 or not s:
            return 0

        j = 0
        total = 0
        min_length = sum(nums)
        set_or_not = False

        for i in range(len(nums)):
            while j < len(nums):
                if j < len(nums) and total < s:
                    total += nums[j]
                    j += 1
                else:
                    break

            if total >= s and j - i <= min_length:
                set_or_not = True
                min_length = j - i

            total -= nums[i]

        if set_or_not:
            return min_length
        else:
            return 0
