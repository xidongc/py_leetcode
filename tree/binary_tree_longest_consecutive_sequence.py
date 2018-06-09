# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        self.helper(root, root.left, 1)
        self.helper(root, root.right, 1)
        return self.res
        
    def helper(self,prev,root,temp):
        if not root:
            self.res = max(self.res,temp)
            return None
        if prev.val + 1 == root.val:
            self.helper(root,root.left,temp+1)
            self.helper(root,root.right,temp+1)
        else:
            self.res = max(self.res,temp)
            self.helper(root,root.left,1)
            self.helper(root,root.right,1)
