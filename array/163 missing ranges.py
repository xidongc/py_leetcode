class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res= []
        if lower > upper:
            return []
        if not nums or nums[0] > upper or nums[-1] < lower:
            return [str(lower) + '->' + str(upper)] if lower < upper else [str(lower)]
        start = lower
        for i in range(len(nums)):
            if nums[i] < start:
                continue
            elif nums[i] == start:
                start += 1
                continue
            res.append(self.getRange(start,nums[i] - 1))
            start = nums[i] + 1
        if start <= upper:
            res.append(self.getRange(start, upper))

        return res
    def getRange(self,num1,num2):
        return str(num1) + '->' + str(num2) if num1 < num2 else str(num1)