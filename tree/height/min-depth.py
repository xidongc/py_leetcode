class Solution(object):

    def minDepth(self, root):

        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        # corner case
        if left_depth == 0 or right_depth == 0:
            return left_depth + right_depth + 1

        return min(left_depth, right_depth) + 1
