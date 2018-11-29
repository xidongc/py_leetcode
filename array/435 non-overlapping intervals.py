# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.end)
        res = 1
        e = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start >= e:
                res += 1
                e = intervals[i].end
        return len(intervals) - res


# interval greedy
# https://en.wikipedia.org/wiki/Interval_scheduling#Interval_Scheduling_Maximization