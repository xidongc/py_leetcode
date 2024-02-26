class Solution(object):
    def search(self, nums, target: int) -> int:
        start, end = 0, len(nums) - 1

        while start < end - 1:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            elif nums[mid] < nums[end]:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        return -1


# 先把在同一侧的情况挑出来，再分析剩下两种情况
class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # One side, 括号必须加
            if (nums[mid] < nums[0]) == (target < nums[0]):
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            elif target < nums[0]:
                start = mid + 1
            else:
                end = mid - 1
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

