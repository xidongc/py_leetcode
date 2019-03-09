import queue,collections


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

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
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
            return True
        else:
            return False
# lmf
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        preDict = collections.defaultdict(set)
        aspreDict = collections.defaultdict(set)
        for i,j in prerequisites:
            preDict[i].add(j)
            aspreDict[j].add(i)
        bfs = [c for c in range(numCourses) if not preDict[c]]
        for pre in bfs:
            for course in aspreDict[pre]:
                preDict[course].remove(pre)
                if not preDict[course]:
                    bfs += [course]
        return len(bfs) == numCourses


# code in 2rd review:
class Solution(object):

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if numCourses == 0:
            return True
        elif len(prerequisites) == 0:
            return True

        inDegree = dict()
        queue = list()
        neighbors = dict()
        seq = list()

        for prerequisite in prerequisites:
            inDegree[prerequisite[0]] = 0
            inDegree[prerequisite[1]] = 0
            neighbors[prerequisite[0]] = []
            neighbors[prerequisite[1]] = []

        for prerequisite in prerequisites:
            inDegree[prerequisite[1]] = inDegree.get(prerequisite[1], 0) + 1
            tmp = neighbors.get(prerequisite[0], [])
            tmp.append(prerequisite[1])

        for k, v in inDegree.items():
            if v == 0:
                queue.append(k)
                seq.append(k)

        while len(queue) > 0:
            ele = queue.pop(0)
            for x in neighbors[ele]:
                inDegree[x] -= 1
                if inDegree[x] == 0:
                    queue.append(x)
                    seq.append(x)

        if len(seq) == len(inDegree) or len(seq) >= numCourses:
            return True
        return False





