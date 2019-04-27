class Solution(object):

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # save both max and min value, sol compared to max subarray
        if len(nums) == 0:
            return 0

        maxN = nums[0]
        minN = nums[0]
        output = nums[0]

        for num in nums[1:]:
            tmpMax = maxN
            tmpMin = minN
            maxN = max(tmpMax, tmpMin, 1) * num
            minN = min(tmpMax, tmpMin, 1) * num
            output = max(output, maxN)
        return output
