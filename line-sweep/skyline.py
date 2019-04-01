
import heapq

class Ele(tuple):

    def __new__(cls, val:tuple):
        return super(Ele, cls).__new__(cls, val)

    def __lt__(self, other):
        START = 0
        END = 1
        if self[0] != other[0]:
            return self[0] < other[0]
        else:
            if self[2] == START and other[2] == START:
                return other[1] < self[1]
            if self[2] == END and other[2] == END:
                return other[1] > self[1]
            else:
                return self[2] == START

    def __le__(self, other):
        return self == other


class Solution(object):

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings or len(buildings) <= 0:
            return []

        START = 0
        END = 1

        tmp = list()
        heap = []

        for b in buildings:
            tmp.append(Ele((b[0], b[2], START, b[1])))
            tmp.append(Ele((b[1], b[2], END, b[1])))

        tmp.sort()

        cityscape = [[tmp[0][0], tmp[0][1]]]
        h = tmp[0][1]
        print(tmp)

        for t in tmp:
            loc = t[0]
            if t[2] == START:
                heapq.heappush(heap, (-t[1], t[3]))
            hello = [0, 0]
            while len(heap) > 0 and loc >= hello[1]:
                hello = heapq.heappop(heap)
            if len(heap) == 0 and loc >= hello[1] and [loc, 0] not in cityscape:
                cityscape.append([loc, 0])
            elif hello[1] != 0:
                heapq.heappush(heap, hello)
                curr = -hello[0]
                if curr != h:
                    cityscape.append([t[0], curr])
                    h = curr
        return cityscape

s = Solution()
buildings = [[1,2,1],[1,2,2],[1,2,3]]
print(s.getSkyline(buildings))