# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 这里不要试图root值去加右边子树的最大值，远比维护一个全局变量麻烦的多
        Solution.sum = 0
        def traverse(root):
            if not root:
                return
            traverse(root.right)
            Solution.sum += root.val
            root.val = Solution.sum
            traverse(root.left)
        traverse(root)
        return root
