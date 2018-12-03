from collections import deque


class Solution(object):
    # Sol-1 using deque to lazy calculate the max avr

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if not nums or len(nums) < k:
            return 0
        q = deque(maxlen=k)
        max_avr = avr = sum(nums[0:k]) / k
        for i, num in enumerate(nums):
            if i >= k:
                avr += (num - q.popleft())/k
                max_avr = max(max_avr, avr)
            q.append(num)
        return max_avr
