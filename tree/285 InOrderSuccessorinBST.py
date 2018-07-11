# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        inorder = []

        def inTraverse(root):
            if not root:
                return
            inTraverse(root.left)
            inorder.append(root.val)
            inTraverse(root.right)

        inTraverse(root)
        pos = inorder.index(p.val)
        return None if pos < 0 or pos == len(inorder) - 1 else inorder[pos + 1]

# ?????????????????????????????????????????????????/