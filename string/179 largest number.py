class LargerNumberKey(str):

    def __lt__(self, other):
        return self + other > other + self


class Solution(object):

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [LargerNumberKey(num) for num in nums]
        nums.sort()

        # corner case for "00" -> "0"
        return "0" if nums[0] == '0' else "".join(nums)
