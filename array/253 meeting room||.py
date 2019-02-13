# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# 本质是判断最多overlap（共存）的room有几个
import collections


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        res = 0
        tmp = 0
        map = collections.defaultdict(int)
        for interval in intervals:
            map[interval.start] += 1
            map[interval.end] -= 1
        for key in sorted(map.keys()):
            tmp += map[key]
            res = max(res, tmp)
        return res


    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x:x.start)
        heap = []  # stores the end time of intervals
        for i in intervals:
            if heap and i.start >= heap[0]:
                # means two intervals can use the same room
                heapq.heapreplace(heap, i.end)
            else:
                # a new room is allocated
                heapq.heappush(heap, i.end)
        return len(heap)