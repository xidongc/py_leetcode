# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ret = list()

        def inOrder(root, k):
            nonlocal ret
            if root is None:
                return
            inOrder(root.left, k)
            ret.append(root.val)
            inOrder(root.right, k)
        inOrder(root, k)
        return ret[k-1]