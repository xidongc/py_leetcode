# https://www.lintcode.com/problem/meeting-rooms-ii/description


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Ele(tuple):

    def __new__(cls, val):
        return super(Ele, cls).__new__(cls, val)

    def __lt__(self, other):
        if self[0] < other[0]:
            return True
        elif self[0] > other[0]:
            return False
        else:
            return self[1] > other[1]

    def __eq__(self, other):
        if self == other:
            return True
        return False

# cxd
class Solution(object):
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        Start = 0
        End = 1
        helper = list()
        max_rooms = 0

        if not intervals or len(intervals) == 0:
            return max_rooms

        for interval in intervals:
            helper.append(Ele((interval.start, Start)))
            helper.append(Ele((interval.end, End)))

        helper.sort()
        num = 0
        for h in helper:
            if h[1] == Start:
                num += 1
            else:
                num -= 1
            max_rooms = max(max_rooms, num)
        return max_rooms


# lmf
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




