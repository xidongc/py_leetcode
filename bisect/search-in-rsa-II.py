class Solution(object):

    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False

        nums = self.removedup(nums)
        start = 0
        end = len(nums) - 1

        while start < end - 1:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            elif nums[start] == target:
                return True
            elif nums[end] == target:
                return True
            elif nums[mid] > nums[start]:
                if nums[start] < target < nums[mid]:
                    end = mid
                elif target > nums[mid] or target < nums[end]:
                    start = mid
                else:
                    return False
            elif nums[mid] < nums[end]:
                if nums[mid] < target < nums[end]:
                    start = mid
                elif target < nums[mid] or target > nums[start]:
                    end = mid
                else:
                    return False

        if nums[start] == target or nums[end] == target:
            return True
        return False

    def removedup(self, nums):
        p1 = 0
        p2 = 0
        while p2 < len(nums):
            if nums[p1] == nums[p2]:
                p2 += 1
            elif nums[p1] != nums[p2]:
                p1 += 1
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 += 1
        return nums[0:p1 + 1]
