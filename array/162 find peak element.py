class Solution(object):

    def findPeakElement(self, nums):
        # binary search Time Complexity: O(log n)
        # Given an input array nums, where nums[i] ≠ nums[i+1]
        start = 0
        end = len(nums) - 1
        while start < end - 1:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid + 1]:
                end = mid - 1
            elif nums[mid] < nums[mid + 1]:
                start = mid + 1

        return start if nums[start] > nums[end] else end
