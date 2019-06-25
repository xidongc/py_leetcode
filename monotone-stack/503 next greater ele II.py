class Solution(object):

    def nextGreaterElements(self, nums):
        # corner case
        if len(nums) == 0:
            return list()

        stack = list()
        res = list()

        for i in range(len(nums) - 1, -1, -1):
            stack.append(i)

        for i in range(len(nums) - 1, -1, -1):
            while len(stack) > 0 and nums[i] >= nums[stack[-1]]:
                stack.pop()
            if len(stack) == 0:
                res.insert(0, -1)
            else:
                res.insert(0, nums[stack[-1]])
            stack.append(i)

        return res
