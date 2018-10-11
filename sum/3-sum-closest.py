# cxd
class Solution:

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ret = nums[0] + nums[1] + nums[-1]
        value = abs(nums[0] + nums[1] + nums[-1] - target)
        i = 0

        while i < len(nums)-2:
            k = len(nums)-1
            j = i+1
            while j < k:
                if abs(nums[i] + nums[j] + nums[k] - target) < value:
                    ret = nums[i] + nums[j] + nums[k]
                    value = abs(nums[i] + nums[j] + nums[k] - target)

                if nums[i] + nums[j] + nums[k] - target > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] - target < 0:
                    j += 1
                else:
                    # value = 0
                    return nums[i] + nums[j] + nums[k]

            i += 1
            while i < len(nums)-2 and nums[i] == nums[i-1]:
                i += 1
        return ret
# lmf
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        res = 2**32 - 1
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return target
                elif sum > target:
                    k -= 1
                else:
                    j += 1
                res = sum if abs(sum - target) < abs(res - target) else res
        return res

s = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(s.threeSumClosest(nums, target))
