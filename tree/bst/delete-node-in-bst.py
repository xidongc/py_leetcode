# Definition for a binary tree node
# .
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findNode(self, root, key):
        if root is None:
            return
        if root.val == key:
            return root
        elif root.val < key:
            self.findNode(root.right, key)
        elif root.val > key:
            self.findNode(root.left, key)

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            minNode = self.findMin(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)
        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node
