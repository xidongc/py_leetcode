# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        con_1 = (p.val == q.val)
        con_2 = self.isSameTree(p.left, q.left)
        con_3 = self.isSameTree(p.right, q.right)
        if con_1 and con_2 and con_3:
            return True
        else:
            return False