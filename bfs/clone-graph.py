# Definition for a undirected graph node
from copy import deepcopy

class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution(object):
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None

        q1 = []
        q2 = []
        head = UndirectedGraphNode(node.label)
        q1.append(node)
        q2.append(head)
        # 用map因为必须要把新的object存起来
        map = {node: head}

        while len(q1) > 0:
            tmp1 = q1.pop(0)
            tmp2 = q2.pop(0)

            if tmp1:
                for i in tmp1.neighbors:
                    if i in map:
                        tmp2.neighbors.append(map[i])
                    else:
                        val2 = UndirectedGraphNode(i.label)
                        map[i] = val2
                        tmp2.neighbors.append(val2)
                        q1.append(i)
                        q2.append(val2)
        return head

# lmf
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        queue = [node]
        head = UndirectedGraphNode(node.label)
        nodeDict = {node: head}
        while queue:
            old = queue.pop(0)
            new = nodeDict[old]
            for neighbor in old.neighbors:
                if neighbor not in nodeDict:
                    queue.append(neighbor)
                    newNeighbor = UndirectedGraphNode(neighbor.label)
                    nodeDict[neighbor] = newNeighbor
                new.neighbors.append(nodeDict[neighbor])
        return head

