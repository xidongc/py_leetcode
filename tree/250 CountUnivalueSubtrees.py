# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        if self.dfs(root, root.val): res += 1
        return self.countUnivalSubtrees(root.left) + self.countUnivalSubtrees(root.right) + res

    def dfs(self, root, value):
        if not root:
            return True
        return root.val == value and self.dfs(root.left, value) and self.dfs(root.right, value)
# 和pathsum||| 一个道理
# # 如何优化？
# Input:  root = [5,1,5,5,5,null,5]
#
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
#
# Output: 4 : 5, 5, 5, 5-5