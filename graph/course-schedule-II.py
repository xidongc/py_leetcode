import queue


class Graph(object):

    def __init__(self, v, e: dict):
        self.v = len(v)
        self.e = len(e)
        self.map = {}
        self.into = {}

        # initialize
        for node in v:
            self.map[node] = []
            self.into[node] = 0

        for edge in e:
            v2, v1 = edge
            # v1->v2
            self.map.get(v1, []).append(v2)
            self.into[v2] += 1

    def get_neighbours(self, node):
        return self.map.get(node, [])

    def get_zero_into(self):
        ret = []
        for k, v in self.into.items():
            if v == 0:
                ret.append(k)
        return ret

    def get_node_into(self, node):
        return self.into[node]

    def change_node_into(self, node, value):
        if value is not None:
            self.into[node] = value


class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        v = range(numCourses)
        g = Graph(v, prerequisites)

        q = queue.Queue()
        sort_result = []
        nodes = g.get_zero_into()
        for node in nodes:
            q.put(node)
            sort_result.append(node)

        while not q.empty():
            n = q.get()
            for i in g.get_neighbours(n):
                tmp = g.get_node_into(i)
                g.change_node_into(i, tmp-1)
                if tmp - 1 == 0:
                    q.put(i)
                    sort_result.append(i)

        if len(sort_result) == numCourses:
            return sort_result
        else:
            print(len(sort_result))
            return []