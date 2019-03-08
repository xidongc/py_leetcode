# Definition for a binary tree node.
# 建立无向图，在每一层把自己和孩子的关系加入dict。然后从target开始bfs向外一圈一圈遍历
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        "


root = TreeNode(1)
root.left = TreeNode(3)
root.left = TreeNode(2)
s = Solution()
s.findClosestLeaf(root)