# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        Solution.sum = 0
        self.helper(root,False)
        return Solution.sum
    def helper(self,root,flag):
        if not root:
            return
        if flag == True and root.left == None and root.right == None:
            Solution.sum += root.val
        self.helper(root.left,True)
        self.helper(root.right,False)
        
            3
           / \
          9  20
            /  \
           15   7
           return 9 + 15  = 24
