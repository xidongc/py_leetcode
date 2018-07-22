# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = 0

        if not root:
            return s

        def _dfs(root, curr):

            nonlocal s
            if root is None:
                return
            if not root.left and not root.right:
                l = len(curr)-1
                s += sum([x.val*(10**(l-i)) for i, x in enumerate(curr)])
            for x in [root.left, root.right]:
                curr.append(x)
                _dfs(x, curr)
                curr.pop()

        _dfs(root, [root])

        return s

