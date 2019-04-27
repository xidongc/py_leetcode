import math


class Solution(object):

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = 0
        if not root:
            return ret

        leftmost = rightmost = 0
        left = right = root

        while left is not None:
            leftmost += 1
            left = left.left

        while right is not None:
            rightmost += 1
            right = right.right

        if rightmost == leftmost:
            return int(math.pow(2, leftmost)) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
