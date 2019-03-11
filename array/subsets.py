class Solution(object):

    def subsets(self, nums):

        def dfs(nums, stack, ret):
            ret.append(stack[:])

            for i, num in enumerate(nums):
                stack.append(num)
                dfs(nums[i + 1:], stack, ret)
                stack.pop()

        stack = list()
        ret = list()
        nums.sort()
        dfs(nums, stack, ret)
        return ret
