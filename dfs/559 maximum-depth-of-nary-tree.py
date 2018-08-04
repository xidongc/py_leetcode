"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        res = 1
        for child in root.children:
            if not child:
                return 1
            res = max(res, 1 + self.maxDepth(child))

        return res