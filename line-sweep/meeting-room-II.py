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






