# position = bisect.bisect(l, r)
# bisect.insort(l, r)
# 14    0 [14]
#  85    1 [14, 85]
# 354 russian doll envelopes
# 找tail中》= num的那个数
import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tail = [0] * len(nums)
        size = 0
        for num in nums:
            i,j = 0,size
            while i != j:
                m = (i + j) // 2
                if num > tail[m]:
                    i = m + 1
                else:
                    j = m
            tail[i] = num
            size = max(size,i + 1)
        return size
nums = [4,10,4,3,8,9]
s = Solution()
print(s.lengthOfLIS(nums))


