class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """

    def max_average(self, nums, k: int) -> float:
        left, right = min(nums), max(nums)

        while left < right - 1e-5:
            mid = left + (right - left) / 2
            if self.isValid(mid, nums[:], k):
                left = mid
            else:
                right = mid
        return left

    def isValid(self, avg, nums, k):
        for i in range(len(nums)):
            nums[i] = nums[i] - avg
        for i in range(1, k):
            nums[i] += nums[i - 1]
            if i == k-1 and nums[i] >= 0:
                return True
        for i in range(k, len(nums)):
            nums[i] += nums[i - 1]
            if nums[i] - min(nums[0:i - k + 1]) >= 0:
                return True
        return False
