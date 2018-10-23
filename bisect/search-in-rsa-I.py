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