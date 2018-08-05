# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
            return ret

        def helper(root):
            if root is None:
                return
            helper(root.left)
            helper(root.right)
            ret.append(root.val)

        helper(root)
        return ret