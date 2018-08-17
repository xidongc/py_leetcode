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
print(s.threeSumClosest([1,1,-1,-1,3],3))
