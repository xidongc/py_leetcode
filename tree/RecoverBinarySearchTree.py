# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):

    def recoverTree(self, root):
        Solution.firstNode = TreeNode(None)
        Solution.secondNode = TreeNode(None)
        Solution.prevNode = TreeNode(-12345678)
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        value = Solution.firstNode.val
        Solution.firstNode.val = Solution.secondNode.val
        Solution.secondNode.val = value
        
        
    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        if Solution.firstNode.val == None and Solution.prevNode.val > root.val:
            Solution.firstNode = Solution.prevNode
        if Solution.firstNode.val != None and Solution.prevNode.val > root.val:
            Solution.secondNode = root
        Solution.prevNode = root
        self.traverse(root.right)

        
