# the same with graph valid tree, DSU data structure can be used in circle detection
# also could use DFS and BFS


class Solution(object):
    def __init__(self):
        self.father = dict()
        self.follower = dict()

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        hashmap = dict()

        if len(edges) < 1:
            return None

        for edge in edges:
            root_0, root_1 = edge

            if edge[0] in hashmap.keys():
                root_0 = self.find(edge[0])
            else:
                self.father[edge[0]] = edge[0]
                hashmap[edge[0]] = True
                self.follower[edge[0]] = 1

            if edge[1] in hashmap.keys():
                root_1 = self.find(edge[1])
            else:
                self.father[edge[1]] = edge[1]
                hashmap[edge[1]] = True
                self.follower[edge[1]] = 1

            if root_0 != root_1:
                self.union(root_0, root_1)
            else:
                return edge

    def find(self, p):
        if p == self.father[p]:
            return p
        self.father[p] = self.find(self.father[p])
        return self.father[p]

    def union(self, p1, p2):
        follower_1 = self.follower.get(p1, 1)
        follower_2 = self.follower.get(p2, 1)
        if self.father[p1] != self.father[p2]:
            if follower_1 >= follower_2:
                self.father[self.father[p2]] = self.father[p1]
                self.follower[p1] = follower_1 + follower_2
            else:
                self.father[self.father[p1]] = self.father[p2]
                self.follower[p2] = follower_2 + follower_1


s = Solution()
a = [[1,2],[1,3],[2,3]]
print(s.findRedundantConnection(a))