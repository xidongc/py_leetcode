class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(stack, ret, nums):
            if len(stack) == len(nums):
                ret.append(stack[:])

            for num in nums:
                if num not in stack:
                    stack.append(num)
                    helper(stack, ret, nums)
                    stack.pop()

        stack = list()
        ret = list()
        helper(stack, ret, nums)
        return ret
