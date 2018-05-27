# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curr = [root]
        self.dfs(root, curr)
        return self.max_depth

    def dfs(self, root, curr):
        if root is None:
            self.max_depth = max(self.max_depth, len(curr))
        elif root.left is not None:
            curr.append(root.left)
            self.dfs(root.left, curr)
            curr.pop()
        elif root.left is not None:
            curr.append(root.left)
            self.dfs(root.right, curr)
            curr.pop()
