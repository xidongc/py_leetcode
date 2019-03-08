# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#这里主要注意判断叶子，并不是not node就代表上一级是leaf，有可能只有一边子树
class Solution:

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if not root:
            return False

        ret = []
        curr = [root.val]

        def dfs(root, sum):
            if sum == 0 and root.left is None and root.right is None:
                ret.append(curr[:])
                print(curr)
            for n in [root.left, root.right]:
                if n is not None:
                    curr.append(n.val)
                    dfs(n, sum-n.val)
                    curr.pop()

        dfs(root, sum-root.val)
        if ret:
            return True
        else:
            return False
        # method 2
        if not root:
            return False
        if not root.left and not root.right and sum == root.val:
            return True
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)

