# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(min, max, node):
            if node is None:
                return True
            con1 = (min < node.val < max)
            con2 = helper(min, node.val, node.left)
            con3 = helper(node.val, max, node.right)
            return con1 and con2 and con3

        return helper(float("-inf"), float("inf"), root)
