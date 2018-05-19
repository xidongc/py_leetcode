class Solution:

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        if len(nums) < 4:
            return ret
        else:
            nums.sort()
            i = 0
            while i < len(nums) - 3:
                t = len(nums)-1
                while t >= 3:
                    j = i+1
                    k = t-1
                    while j < k:
                        if nums[i] + nums[j] + nums[k] + nums[t] - target > 0:
                            k -= 1
                        elif nums[i] + nums[j] + nums[k] + nums[t] - target < 0:
                            j += 1
                        else:
                            ret.append((nums[i], nums[j], nums[k], nums[t]))
                            j += 1
                            k -= 1
                            while j < k and nums[k] == nums[k+1]:
                                k -= 1
                            while j < k and nums[j] == nums[j-1]:
                                j += 1

                    t -= 1
                    while t >= 3 and nums[t] == nums[t+1]:
                        t -= 1
                i += 1
                while i < len(nums) - 3 and nums[i] == nums[i-1]:
                    i += 1

            return list(set(ret))

s = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(s.fourSum(nums, target))
