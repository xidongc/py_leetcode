#这个好难啊
#因为python3没有max min value 目前只能用123456789这个蠢办法
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        res = self.largestBST(root)
        return res[2]
    def largestBST(self,root):
        if not root:
            return [123456789,-123456789,0]
        left = self.largestBST(root.left)
        right = self.largestBST(root.right)
        if root.val > left[1] and root.val < right[0]:
            return [min(left[0],root.val),max(right[1],root.val),left[2]+right[2]+1]
        else:
            return [-123456789,123456789,max(left[2],right[2])]
        
    
        
