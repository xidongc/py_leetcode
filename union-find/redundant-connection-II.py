# refer to https://leetcode.com/problems/redundant-connection-ii/discuss/183541/Python-Union-Find-solution-amortized-O(n)-with-explanation


class Solution(object):

    def __init__(self):
        self.father = dict()
        self.parent = dict()

    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        hashmap = dict()
        has_circle = False
        start = end = None

        if len(edges) < 1:
            return None

        for edge in edges:
            if edge[1] in self.parent.keys():
                start = [self.parent[edge[1]], edge[1]]
                end = edge

            else:
                root_0, root_1 = edge
                self.parent[edge[1]] = edge[0]

                if edge[0] in hashmap.keys():
                    root_0 = self.find(edge[0])
                else:
                    self.father[edge[0]] = edge[0]
                    hashmap[edge[0]] = True

                if edge[1] in hashmap.keys():
                    root_1 = self.find(edge[1])
                else:
                    self.father[edge[1]] = edge[1]
                    hashmap[edge[1]] = True

                if root_0 == root_1:
                    # have loop
                    if not start:
                        start = edge
                    has_circle = True
                self.union(root_0, root_1)

        if has_circle:
            return start
        else:
            return end

    def find(self, p):
        if p == self.father[p]:
            return p
        self.father[p] = self.find(self.father[p])
        return self.father[p]

    def union(self, p1, p2):
        if self.father[p1] != self.father[p2]:
            self.father[self.father[p1]] = self.father[p2]


s = Solution()
a = [[3, 4], [4, 1], [1, 2], [2, 3], [5, 1]]
print(s.findRedundantDirectedConnection(a))