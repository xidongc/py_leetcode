# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = [[]for _ in range(self.getHeight(root))]
        self.dfs(root, ret, self.getHeight(root)-1)
        return ret

    def getHeight(self, root):
        if root is None:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        return max(left, right) + 1

    def dfs(self, root, ret, level):
        if root is None:
            return
        ret[level].append(root.val)
        self.dfs(root.left, ret, level-1)
        self.dfs(root.right, ret, level-1)