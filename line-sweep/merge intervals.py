class Solution(object):

    def merge(self, intervals):
        # corner case
        if len(intervals) == 0:
            return list()

        start, end = 0, 1
        times = list()

        for i in intervals:
            times.append((i[0], start))
            times.append((i[1], end))

        times.sort()
        cnt = 0
        start_time =  -1
        output = list()

        for t in times:
            if t[1] == start:
                if cnt == 0:
                    start_time = t[0]
                cnt += 1
            elif t[1] == end:
                cnt -= 1
                if cnt == 0:
                    end_time = t[0]
                    output.append((start_time, end_time))
        return output
