# have tried tree level traversal, need to consider 4 possible max


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def rob(self, root):
        return max(self.helper(root))

    def helper(self, root):
        if root is None:
            return 0, 0
        lchild, lval = self.helper(root.left)
        rchild, rval = self.helper(root.right)

        return lval+rval, max(lval+rval, lval+rchild, rval+lchild, lchild+rchild+root.val)




