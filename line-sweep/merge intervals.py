class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def merge(self, intervals):
        # skyline problem

        # corner case
        if len(intervals) == 0:
            return list()

        skyline = list()
        for interval in intervals:
            skyline.append((interval.start, 1))
            skyline.append((interval.end, 2))

        skyline.sort(key=lambda a: (a[0], a[1]))
        flying = 0
        start = skyline[0][0]
        ret = list()
        for (ele, status) in skyline:
            if status == 2:
                flying -= 1;
                if flying == 0:
                    ret.append([start, ele])
            elif status == 1:
                if flying == 0:
                    start = ele
                flying += 1
        return ret
