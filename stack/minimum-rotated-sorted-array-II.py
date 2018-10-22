class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        start = 0
        end = len(nums)-1
        min_val = nums[0]
        if nums[start] < nums[end]:
            return min_val

        while start < end - 1:
            mid = start + (end-start)//2
            if nums[start] < nums[mid]:
                min_val = min(min_val, nums[start])
                start = mid + 1
            elif nums[start] > nums[mid]:
                min_val = min(min_val, nums[mid])
                end = mid - 1
            else:
                start += 1

        return min(min_val, nums[start], nums[end])

s = Solution()
print(s.findMin([14,15,1,2,3]))
