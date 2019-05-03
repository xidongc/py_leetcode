# sol-1 dfs
class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = list()

        def helper(stack, nums):
            nonlocal ret
            if len(stack) == len(nums):
                ret.append(stack[:])

            for num in nums:
                if num not in stack:
                    stack.append(num)
                    helper(stack, nums)
                    stack.pop()

        stack = list()
        ret = list()
        helper(stack, nums)
        return ret


# sol-2 leverage next permutation
class Solution(object):

    def permute(self, nums):

        def nextPermutation(nums):

            i = len(nums) - 1
            j = 0

            while i > 0:
                if nums[i - 1] < nums[i]:
                    j = i - 1
                    break
                i -= 1

            for i in range(len(nums) - 1, j, -1):
                if nums[i] > nums[j]:
                    break

            nums[i], nums[j] = nums[j], nums[i]
            nums[j + 1:] = sorted(nums[j + 1:])
            return nums

        output = list()
        nums.sort()
        val = nums
        while val not in output:
            # deep copy of val
            output.append(val[:])
            val = nextPermutation(val)
        return output
