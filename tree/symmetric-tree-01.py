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
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        ret = False
        if left is None and right is None:
            ret = True
        con1 = (left.val == right.val)
        con2 = (self.helper(left.left, right.right))
        con3 = (self.helper(left.right, right.left))
        if con1 and con2 and con3:
            ret = True
        return ret


