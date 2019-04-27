class Solution(object):

    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = 0

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sumN = nums[i] + nums[j] + nums[k]
                if sumN >= target:
                    k -= 1
                elif sumN < target:
                    count += (k - j)
                    j += 1
        return count
