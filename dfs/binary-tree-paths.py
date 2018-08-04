# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        sol = []
        if not root:
            return sol

        def __dfs__(node, curr):
            if node is None:
                return

            if not node.left and not node.right:
                s = str(curr[0].val)
                for x in curr[1:]:
                    tmp = "->" + str(x.val)
                    s += tmp
                sol.append(s)

            for x in [node.left, node.right]:
                curr.append(x)
                __dfs__(x, curr)
                curr.pop()

        curr = [root]
        __dfs__(root, curr)
        return sol
