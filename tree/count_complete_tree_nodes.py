# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution 1 by Hui Jiang:

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


# Solution 2 by Xidong:

class Solution(object):

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = 0

        if not root:
            return ret

        def get_height(root):
            if root is None:
                return 0
            return get_height(root.left) + 1

        for i in range(get_height(root)):
            ret += 2**i

        def helper(root):
            if get_height(root.left) > get_height(root.right):
                nonlocal ret
                helper(root.left)
                ret -= 2**get_height(root.left)//2
                if root.right is None:
                    return
            else:
                if root.right is None:
                    return
                helper(root.right)

        helper(root)
        return ret
