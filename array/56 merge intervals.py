# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: (x.start, x.end))
        res = []
        start, end = -1, -1
        for interval in intervals:
            if interval.start <= end:
                end = max(interval.end, end)
            else:
                if start != -1 and end != -1:
                    res.append((start, end))
                start, end = interval.start, interval.end
        res.append((start, end))
        return res
# [1,4],[2,3]
# [1,4],[2,6]
# [1,4],[0,0]
