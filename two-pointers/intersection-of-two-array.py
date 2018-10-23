class Solution:

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = []
        nums1.sort()
        nums2.sort()

        p1 = 0
        p2 = 0

        while p1 <= len(nums1)-1 and p2 <= len(nums2) -1 :
            if nums1[p1] == nums2[p2]:
                if nums1[p1] not in ret:
                    ret.append(nums1[p1])
                p1 += 1