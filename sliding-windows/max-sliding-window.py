# Sol-1 using decrease monotone stack


class Solution(object):

    def maxSlidingWindow(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        stack = list()
        d = dict()
        result = list()

        for i, num in enumerate(nums):
            if len(stack) == 0:
                stack.append(num)
            else:
                while len(stack) > 0 and stack[-1] <= num:
                    stack.pop()
                stack.append(num)
            d[num] = i

            if i >= k-1:
                while len(stack) > 0:
                    if i+1-k <= d[stack[0]]:
                        result.append(stack[0])
                        break
                    else:
                        stack.pop(0)

        return result





