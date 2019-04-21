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


# Sol-2 iterative solution with stack
# Definition for a binary tree node.
class Solution(object):

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # corner case
        if root is None:
            return list()

        parent = dict()
        parent[root] = None

        stack = list()
        stack.append(root)
        output = list()

        while len(stack) > 0:
            curr = stack.pop()

            if not curr.left and not curr.right:
                # leaf node here
                output.append(self.getTreePath(curr, parent))

            if curr.right:
                stack.append(curr.right)
                parent[curr.right] = curr
            if curr.left:
                stack.append(curr.left)
                parent[curr.left] = curr

        return output

    def getTreePath(self, curr, parent):
        tmp = list()
        while curr:
            tmp.insert(0, curr.val)
            curr = parent[curr]
        return "->".join([str(t) for t in tmp])
