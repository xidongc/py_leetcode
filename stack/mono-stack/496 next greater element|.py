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

    # mono stack
    # from left to right
    def next_greater_element(self, nums1, nums2):
        mappings = {x: i for i, x in enumerate(nums1)}
        mono_stack = []
        results = [-1] * len(nums1)
        for num in nums2:
            while mono_stack and mono_stack[-1] < num:
                ele = mono_stack.pop()
                if ele in mappings:
                    results[mappings[ele]] = num
            mono_stack.append(num)
        return results

    # from right to left
    def next_greater_element_2(self, nums1, nums2):
        mappings = {x: i for i, x in enumerate(nums1)}
        mono_stack = []
        results = [-1] * len(nums1)
        for num in nums2[::-1]:
            while mono_stack and mono_stack[-1] < num:
                mono_stack.pop()
            if num in mappings:
                results[mappings[num]] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(num)
        return results
