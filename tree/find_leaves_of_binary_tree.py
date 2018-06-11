# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        Solution.res = []
        self.helper(root)
        return Solution.res
    
    def helper(self,root):
        if not root:
            return -1
        level = 1 + max(self.helper(root.left),self.helper(root.right))
        if len(Solution.res) <= level:
            Solution.res += [[]]
        Solution.res[level] += [root.val]
        root.left = root.right = None
        return level
        
