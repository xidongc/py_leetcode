# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        clist = []
        self.helper(root,clist)
        return clist[k-1]
    
    def helper(self,root,clist):
        if not root:
            return  
        self.helper(root.left,clist)
        clist.append(root.val)
        self.helper(root.right,clist)

   #lmf
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = 0
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            dfs(root.right)
        dfs(root)
        return self.res


root= TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
s = Solution()
s.kthSmallest(root,1)