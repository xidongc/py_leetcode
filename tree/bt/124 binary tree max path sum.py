# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxSum = -float("inf")

        def helper(root):
            nonlocal maxSum
            if root is None:
                return 0
            leftSum = max(0, helper(root.left))
            rightSum = max(0, helper(root.right))
            maxSum = max(maxSum, leftSum + rightSum + root.val)
            return max(leftSum, rightSum) + root.val

        helper(root)

        return maxSum