class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = len(nums)
        # sum(1->n) = n*(n+1)/2TrT
        return num*(num+1)/2 - sum(nums)