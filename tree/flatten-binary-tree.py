# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        curr = []
        head = root

        def dfs(root):
            nonlocal head
            if root is None:
                return
            else:
                if curr:
                    head.right = curr[-1]
                    head.left = None
                    head = curr[-1]
            for i in [root.left, root.right]:
                curr.append(i)
                dfs(i)
                curr.pop()

        dfs(root)

# preorder traverse version
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        nodeList = []
        def dfs(root):
            if not root:
                return
            nodeList.append(root)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        for i in range(1,len(nodeList)):
            nodeList[i-1].left = None
            nodeList[i-1].right = nodeList[i]

# dfs version(quicker) reverse preorder traversal
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.prev = None
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            dfs(root.left)
            root.right = self.prev
            root.left = None
            self.prev = root
        dfs(root)
