from random import Random


class Solution(object):
    # Fisher-Yates shuffle with reservoir sampling

    def __init__(self, nums):
        self.rnd = Random()
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        index = None
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if int(self.rnd.random() * count) == 0:
                    index = i
        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
