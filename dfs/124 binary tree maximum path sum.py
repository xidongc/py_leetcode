class Solution(object):

    def maxPathSum(self, root):
        maxValue = float("-inf")

        def helper(root):
            if root is None:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            if left <= 0 and right <= 0:
                self.maxValue = max(maxValue, root.val)
            elif left <= 0:
                self.maxValue = max(maxValue, root.val + right)
            elif right <= 0:
                self.maxValue = max(maxValue, root.val + left)
            else:
                self.maxValue = max(maxValue, root.val + left + right)
            return max(left + root.val, right + root.val, root.val)

        helper(root)
        return maxValue
