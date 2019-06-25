# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue

class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q_left = queue.Queue()
        q_right = queue.Queue()
        q_left.put(root.left)
        q_right.put(root.right)
        while q_left.empty() is not None and q_right is not None:
            left = q_left.get()
            right = q_right.get()
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            if left.val == right.val:
                q_left.put(left.left)
                q_left.put(left.right)
                q_right.put(right.right)
                q_right.put(right.left)
            else:
                return False
