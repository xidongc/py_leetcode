class TreeNode:
    def __init__(self,x):
        TreeNode.val = x
        TreeNode.left = None
        TreeNode.right = None
class Solution:
    def copyTree(self,root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        else:
            node = TreeNode(root.val)
            node.left = self.copyTree(root.left)
            node.right = self.copyTree(root.right)
            return node
