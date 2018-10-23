"""
# BFS topological sort

The actual implementation is similar to the BFS topological sort.
Remove the leaves, update the degrees of inner vertexes.
Then remove the new leaves.
Doing so level by level until there are 2 or 1 nodes left.
What's left is our answer!

The time complexity and space complexity are both O(n).
"""


class Graph(object):

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.mapping = {}
        self.leaves = []

        for node in nodes:
            self.mapping[node] = []

        for edge in edges:
            v1, v2 = edge
            self.mapping[v1].append(v2)
            self.mapping[v2].append(v1)

        for key in self.mapping.keys():
            if len(self.mapping[key]) == 1:
                self.leaves.append(key)

    def find_min_trees(self):
        left_nodes = len(self.nodes)
        while left_nodes > 2:
            new_leaves = []
            for leaf in self.leaves:
                next = self.mapping[leaf].pop()
                self.mapping[next].remove(leaf)
                if len(self.mapping[next]) == 1:
                    new_leaves.append(next)
            left_nodes -= len(self.leaves)
            self.leaves = new_leaves
        return self.leaves


class Solution(object):

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if len(edges) == 0 or not n or not edges:
            return [0]

        g = Graph(range(n), edges)
        return g.find_min_trees()


