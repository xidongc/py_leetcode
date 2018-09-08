# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        if root.val != key:
            root.left = self.deleteNode(root.left, key)
            root.right = self.deleteNode(root.right, key)

        if root.left is None and root.right is None:
            return None

        elif root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        node = self.find_substitute(root)
        root.val = node.val
        self.deleteNode(node.right, node.val)
        return node

    def find_substitute(self, root):
        # find smallest in right sub tree
        tmp = root.right
        while tmp.left:
            tmp = tmp.left
        return tmp

