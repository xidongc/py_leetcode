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
        minValue = -pow(2,32) + 1
        Solution.res = minValue
        def helper(root):
            if not root:
                return minValue
            left = helper(root.left)
            right = helper(root.right)
            Solution.res = max(Solution.res,left,right,left + root.val,right + root.val,root.val, left + right + root.val)
            return max(root.val,left+root.val,right+root.val)
        helper(root)
        return Solution.res
s = Solution()
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s.maxPathSum(root)