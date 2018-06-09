# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        clist = []
        self.helper(root,clist)
        return clist[k-1]
    
    def helper(self,root,clist):
        if not root:
            return  
        self.helper(root.left,clist)
        clist.append(root.val)
        self.helper(root.right,clist)

        
