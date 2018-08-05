# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        p1, p2 = self.morris_in_traversal(root)
        tmp = p1.val
        p1.val = p2.val
        p2.val = tmp

    def morris_in_traversal(self, root):

        current = root
        pre = None
        ret = []
        found = False
        p1 = p2 = None

        while current:
            if current.left is None:
                ret.append(current.val)
                if pre and pre.val > current.val:
                    if not found:
                        found = True
                        p1 = pre
                    p2 = current

                pre = current
                current = current.right

            else:
                prev = current.left
                while prev.right and prev.right is not current:
                    prev = prev.right
                if prev.right is None:
                    prev.right = current
                    current = current.left
                else:
                    prev.right = None
                    ret.append(current.val)
                    if pre and pre.val > current.val:
                        if not found:
                            found = True
                            p1 = pre
                        p2 = current

                    pre = current
                    current = current.right
        return p1, p2

