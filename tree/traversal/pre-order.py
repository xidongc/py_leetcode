# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
            return ret

        def dfs(root):
            if root is None:
                return
            ret.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return ret