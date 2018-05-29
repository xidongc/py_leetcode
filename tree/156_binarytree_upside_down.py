# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # node = TreeNode()
        node = root
        parent = None
        right = None
        while node != None:
            left = node.left
            node.left = right
            right = node.right
            node.right = parent
            parent = node
            node = left
        return parent
            
#         p45
