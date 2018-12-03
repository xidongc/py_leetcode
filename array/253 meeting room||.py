# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
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

