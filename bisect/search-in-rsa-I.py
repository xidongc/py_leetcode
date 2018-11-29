class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        if not nums or len(nums) == 0:
            return -1

        while start < end - 1:
            mid = (end - start)/2 + start
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[end]:
                if target < nums[mid]:
                    end = mid
                elif target < nums[end]:
                    start = mid
                elif target == nums[end]:
                    return end
                elif target < nums[start]:
                    return -1
                elif target == nums[start]:
                    return start
                else:
                    end = mid
            elif nums[mid] > nums[end]:
                if target > nums[mid]:
                    start = mid
                elif target > nums[start]:
                    end = mid
                elif target == nums[start]:
                    return start
                elif target > nums[end]:
                    return -1
                elif target == nums[end]:
                    return end
                else:
                    start = mid

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        return -1

# 先把在同一侧的情况挑出来，再分析剩下两种情况
class Solution(object):
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

