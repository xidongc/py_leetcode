from heapq import *


class Solution(object):

    def smallestRange(self, nums):

        heap = []
        heapify(heap)

        for i, num in enumerate(nums):
            if len(num) == 0:
                return 0
            else:
                heappush(heap, (num[0], i, 0))

        right = max([num[0] for num in nums])
        left = min([num[0] for num in nums])

        tmp_right = right

        while len(heap) > 0:
            (num, chl, i) = heappop(heap)
            if tmp_right - num < right - left:
                left, right = num, tmp_right

            if i == len(nums[chl]) - 1:
                break

            tmp_right = max(tmp_right, nums[chl][i + 1])
            heappush(heap, (nums[chl][i + 1], chl, i + 1))
        return [left, right]
