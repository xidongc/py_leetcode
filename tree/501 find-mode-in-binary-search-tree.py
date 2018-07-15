# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # Use extra space
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        map = {}
        maxTimes = 0
        res = []
        def preTraverse(root):
            if not root:
                return
            if root.val in map:
                map[root.val] += 1
            else:
                map[root.val] = 1
            preTraverse(root.left)
            preTraverse(root.right)
        preTraverse(root)
        for key, value in map.items():
            if value > maxTimes:
                maxTimes = value
                res = [key]
            elif value == maxTimes:
                res.append(key)
        return res
    # No extra space
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
s = Solution()
s.findMode(root)
