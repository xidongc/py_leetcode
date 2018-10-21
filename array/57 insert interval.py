# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)
        start, end = -1, -1
        res = []
        for interval in intervals:
            if interval.start <= end:
                end = max(end, interval.end)
            else:
                if start != -1 and end != -1:
                    res.append((start, end))
                start, end = interval.start, interval.end
        res.append((start, end))
        return res
