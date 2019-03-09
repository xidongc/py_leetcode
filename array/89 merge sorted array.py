class Solution(object):

    def merge(self, nums1, m: int, nums2, n: int):

        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            else:
                nums1[i + j + 1] = nums2[j]
                j -= 1

        while j >= 0:
            nums1[j] = nums2[j]
            j -= 1
