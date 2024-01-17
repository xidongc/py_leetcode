class Solution(object):

    def nextGreaterElement(self, nums1, nums2):
        # corner case
        if len(nums1) > len(nums2):
            return list()

        mono_stack = list()
        hashmap = dict()

        for num in nums2:
            if len(mono_stack) == 0:
                mono_stack.append(num)
            else:
                while len(mono_stack) > 0 and num > mono_stack[-1]:
                    hashmap[mono_stack.pop()] = num
                mono_stack.append(num)

        while len(mono_stack) > 0:
            hashmap[mono_stack.pop()] = -1

        output = list()

        for num in nums1:
            if num in hashmap:
                output.append(hashmap[num])
            else:
                output.append(-1)

        return output
