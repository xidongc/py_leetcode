class Solution:
    def firstMissingPositive(self, nums) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = len(nums) + 1

        for i in range(len(nums)):
            if len(nums) >= abs(nums[i]) > 0:
                if nums[abs(nums[i]) - 1] > 0:
                    nums[abs(nums[i]) - 1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1
