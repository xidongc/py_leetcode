# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Solution.maxDepth = 0
        Solution.res = 0
        def dfs(root, depth):
            if not root:
                return
            dfs(root.left, depth + 1)
            if depth > Solution.maxDepth:
                Solution.res = root.val
                Solution.maxDepth = depth
            dfs(root.right, depth + 1)

        dfs(root, 1)
        return Solution.res
root = TreeNode(2)
root.right = TreeNode(1)
root.right.left = TreeNode(3)
s = Solution()
s.findBottomLeftValue(root)
# root depth is 1, therefore maxdepth has to be lower than 1
