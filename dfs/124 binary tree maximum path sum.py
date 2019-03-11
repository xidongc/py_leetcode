# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# BOTTOM TO TOP
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Solution.res = -(2 ** 32) + 1

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            #             at most one child.
            max_single = max(max(left, right) + root.val, root.val)
            #             complete path
            max_top = max(left + right + root.val, max_single)
            Solution.res = max(max_top, Solution.res)
            #             return single path
            return max_single

        dfs(root)
        return Solution.res
s = Solution()
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s.maxPathSum(root)