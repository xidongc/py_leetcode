# 1）用sort从1开始进2往后遍历，如果i和i-1不一致就是i是单的/else最后一个是单的
# 2）异或
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        nums.sort()
        for i in range(0, len(nums), 2):
            if i + 1 == len(nums):
                return nums[i]
            elif nums[i + 1] != nums[i]:
                return nums[i]


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res
