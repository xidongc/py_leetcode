class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        is_same = [a == b for a,b in zip(nums,sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same[::-1].index(False) - is_same.index(False) 
        
