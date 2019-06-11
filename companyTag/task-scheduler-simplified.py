from heapq import heappush, heappop, heapify


class Solution(object):

    def leastInterval(self, tasks, n):
        hashmap = dict()
        heap = []
        heapify(heap)
        count = 0
        for t in tasks:
            while (len(heap) > 0 and heap[0][0] < count - n):
                hashmap.pop(heappop(heap)[1])
            count = max(count+1, hashmap.get(t, float("-inf")) + n + 1)
            hashmap[t] = count
            heappush(heap, (hashmap[t], t))
        return count
