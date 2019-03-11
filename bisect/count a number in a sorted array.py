# 基础：
#    1. 用二分法找到位置，然后向两边延伸。但是如果array里只有这个数字，复杂度O(n)
# 优化版：
#    2. 用二分法分别找左边第一个，和右边第一个
class Solution:
    def getNumberOfK(self, array, k):
        count = 0
        if array:
            first = self.getFirstK(array,k,0,len(array)-1)
            last = self.getLastK(array, k,0,len(array) - 1)
            if first > -1 and last > -1:
                count = last - first + 1
        return count

    def getFirstK(self,nums,k,start,end):
        if not nums:
            return -1
        while start + 1 < end:
            mid = (start + end) // 2
            num = nums[mid]
            if num == k:
                if mid > 0 and nums[mid-1] != k:
                    return mid
                else:
                    end = mid - 1
            elif num > k:
                end = mid - 1
            else:
                start = mid + 1
        if nums[start] == k:
            return start
        elif nums[end] == k:
            return end
        return -1

    def getLastK(self,nums,k,start,end):
        if not nums:
            return -1
        while start + 1 < end:
            mid = (start + end) // 2
            num = nums[mid]
            if num == k:
                if mid < len(nums)-1 and nums[mid+1] != k:
                    return mid
                else:
                    start = mid + 1
            elif num > k:
                end = mid - 1
            else:
                start = mid + 1
        return -1
        if nums[start] == k:
            return start
        elif nums[end] == k:
            return end
        return -1


