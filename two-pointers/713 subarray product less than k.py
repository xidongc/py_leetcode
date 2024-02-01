# sliding window
class Solution(object):

    # solution with template
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        if k <= 1:
            return 0

        result, product, i, j = 0, 1, 0, 0
        while j < len(nums):
            product *= nums[j]

            while product >= k:
                product /= nums[i]
                i += 1

            result += (j - i + 1)
            j += 1
        return result

    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        pro = 1
        i,j = 0,0
        while j < len(nums):
            if nums[j] < k:
                pro *= nums[j]
                while i <= j and pro >= k:
                    pro /= nums[i]
                    i += 1
                res += j - i + 1
            else:
                pro = 1
                i = j + 1
            j += 1

        return res

s = Solution()
s.numSubarrayProductLessThanK([10,5,2,6],100)