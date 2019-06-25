class Solution(object):

    # two pointers
    def intersect(self, nums1, nums2):

        ret = list()
        nums1.sort()
        nums2.sort()

        p1 = 0
        p2 = 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                ret.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            elif nums2[p2] > nums1[p1]:
                p1 += 1
        return ret


class Solution(object):

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ret = list()
        nums1.sort()
        nums2.sort()

        output = list()
        start = 0

        if len(nums1) < len(nums2):
            for num in nums1:
                i = self.binarySearch(start, nums2, num)
                if i != -1:
                    output.append(nums2[i])
                    start = i + 1
        else:
            for num in nums2:
                i = self.binarySearch(start, nums1, num)
                if i != -1:
                    output.append(nums1[i])
                    start = i + 1
        return output

    def binarySearch(self, i, nums, target):
        start = i
        end = len(nums)
        while start < end - 1:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        if start < len(nums) and nums[start] == target:
            return start
        elif end < len(nums) and nums[end] == target:
            return end
        else:
            return -1
