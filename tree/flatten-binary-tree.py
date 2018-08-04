# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        curr = []
        head = root

        def dfs(root):
            nonlocal head
            if root is None:
                return
            else:
                if curr:
                    head.right = curr[-1]
                    head.left = None
                    head = curr[-1]
            for i in [root.left, root.right]:
                curr.append(i)
                dfs(i)
                curr.pop()

        dfs(root)