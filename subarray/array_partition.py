class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        nums.sort()
        sum = 0
        for i in range(0,len(nums)-1,2):
            sum += min(nums[i],nums[i+1])
        return sum
            
        
