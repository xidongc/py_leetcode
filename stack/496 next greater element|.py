# 503 if rotaiton next greater, then expand the list twice
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        map = dict()
        res = []
        for num in nums2:
            while stack and num > stack[-1]:
                map[stack.pop()] = num
            stack.append(num)
        for num in nums1:
            res.append(map.setdefault(num,-1))
        return res