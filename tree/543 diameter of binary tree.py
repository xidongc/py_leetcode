# 像124
class Solution(object):
    # Sol-1 from rabbit

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Solution.res = 0

        def maxDepth(root):
            if not root:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            Solution.res = max(left+right, Solution.res)
            return max(left, right) + 1
        maxDepth(root)
        return Solution.res


# Sol-2
class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxDepth = 1

        def helper(root):
            nonlocal maxDepth
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            maxDepth = max(maxDepth, left + right + 1)
            return max(left, right) + 1

        helper(root)
        return maxDepth - 1
