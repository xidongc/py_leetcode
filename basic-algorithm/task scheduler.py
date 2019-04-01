from queue import PriorityQueue


class Solution(object):

    def leastInterval(self, tasks, n: int) -> int:

        if len(tasks) <= 0:
            return 0

        cycle = 0
        hashmap = dict()
        pq = PriorityQueue()

        for task in tasks:
            hashmap[task] = hashmap.get(task, 0) + 1

        for x in hashmap.values():
            pq.put(-x)

        while not pq.empty():
            tmp = list()
            for _ in range(n + 1):
                if pq.qsize() > 0:
                    tmp.append(-pq.get())

            for t in tmp:
                if t - 1 > 0:
                    pq.put(-t + 1)

            cycle += len(tmp) if pq.empty() else n + 1
        return cycle
