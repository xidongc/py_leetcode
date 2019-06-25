from collections import deque


class MonoDeque(object):
    # # Sol-1 using decrease monotone stack

    def __init__(self, windowSize):
        self.deq = deque()
        self.windowSize = windowSize

    def append(self, i, ele):
        # clean outdated index
        if len(self.deq) > 0 and self.deq[0][1] <= i - self.windowSize:
            self.deq.popleft()

        while len(self.deq) > 0 and ele >= self.deq[-1][0]:
            self.deq.pop()

        if len(self.deq) == 0 or ele <= self.deq[-1][0]:
            self.deq.append((ele, i))

    def get(self):
        if len(self.deq) > 0:
            return self.deq[0][0]


class Solution(object):

    def maxSlidingWindow(self, nums, k):

        # corner case
        if k > len(nums) or k <= 0:
            return list()
        elif k == 1:
            return nums

        output = list()
        md = MonoDeque(k)
        for i in range(k-1):
            md.append(i, nums[i])

        for i in range(k-1, len(nums)):
            md.append(i, nums[i])
            output.append(md.get())
        return output


s  = Solution()
nums = [1,3,-1,-3,5,3,6,7]
ret = s.maxSlidingWindow(nums, k=3)
print(ret)
