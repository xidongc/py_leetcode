"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        Solution.res = None
        Solution.maxavg = -(2 ** 32) + 1
        def helper(node):
            if not node:
                return 0, 0
            leftsum,leftsize = helper(node.left)
            rightsum,rightsize = helper(node.right)
            cursum,cursize = leftsum + rightsum + node.val, leftsize + rightsize + 1
            curavg = cursum/cursize
            if not Solution.res or Solution.maxavg < curavg:
                Solution.res = node
                Solution.maxavg = curavg
            return curavg,cursize
        helper(root)
        return Solution.res