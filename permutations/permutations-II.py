class Solution(object):

    def permuteUnique(self, nums):

        length = len(nums)

        def helper(stack, ret):
            if len(stack) == length:
                tmp = [nums[i] for i in stack]
                if tmp not in ret:
                    ret.append(tmp)
                return
            elif len(stack) > length:
                return

            for i in range(len(nums)):
                if i not in stack:
                    stack.append(i)
                    helper(stack, ret)
                    stack.pop()

        stack = list()
        ret = list()
        helper(stack, ret)
        return ret

