# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        map = {}
        def dfs(root, depth):
            if not root:
                return
            if depth in map:
                map[depth] = max(map[depth],root.val)
            else:
                map[depth] = root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 1)
        return list(map.values())

root = TreeNode(2)
root.right = TreeNode(1)
root.right.left = TreeNode(3)
s = Solution()
print(s.largestValues(root))