class Solution(object):

    def __init__(self):
        self.ret = True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ret = True
        self.get_tree_height(root, ret)
        return self.ret

    def get_tree_height(self, root, ret):
        if root is None:
            return 0
        left = self.get_tree_height(root.left, ret)
        right = self.get_tree_height(root.right, ret)
        print(left, right)
        self.ret = self.ret and (-1<=left-right<=1)
        return max(left, right) + 1