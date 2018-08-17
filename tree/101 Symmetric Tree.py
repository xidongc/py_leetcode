# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        def dfs(leftNode,rightNode):
            if leftNode == None and rightNode == None:
                return True
            elif leftNode == None or rightNode == None or leftNode.val != rightNode.val:
                return False
            else:
                return dfs(leftNode.left,rightNode.right) and dfs(leftNode.right,rightNode.left)

        return dfs(root.left,root.right)