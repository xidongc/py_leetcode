# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(min, max, node):
            if node is None:
                return True
            con1 = (min < node.val < max)
            con2 = helper(min, node.val, node.left)
            con3 = helper(node.val, max, node.right)
            return con1 and con2 and con3

        return helper(float("-inf"), float("inf"), root)
# lmf
# 中序遍历，1）可以用数组
#          2）省去数组，用prev记录前一个，因为是严格升序所以右子树最左子肯定比node大
class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        Solution.prev = None
        def helper(root):
            if not root:
                return True
            if not helper(root.left):
                return False
            if Solution.prev != None and Solution.prev >= root.val:
                return False
            Solution.prev = root.val
            return helper(root.right)
        return helper(root)

root = TreeNode(0)
root.right = TreeNode(-1)
s = Solution()
print(s.isValidBST(root))
#  5
# 1  4
#   3 6

