"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            tmpval = []
            tmpnode = []
            for node in queue:
                tmpval.append(node.val)
                if node.children:
                    for child in node.children:
                        tmpnode.append(child)
            res.append(tmpval)
            queue = tmpnode
        return res
