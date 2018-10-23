class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 3:
            return False
        smallest = pow(2,32) - 1
        secondsmallest = pow(2, 32) - 1
        for num in nums:
            if num < smallest:
                smallest = num
            elif num > smallest and num < secondsmallest:
                # secondsmallest出现的条件就是左边已经有smallest了
                secondsmallest = num
            if num > secondsmallest:
                return True
        return False

# in this problem we just need to determine whether the subsequence exists.
# so after assigning the value to min and secondMin,
#  even though there might be a smaller value afterward and the variable min gets updated,
#  it does not affect the increasing subsequence overall as long as there is an integer that is larger than 'secondMin'
