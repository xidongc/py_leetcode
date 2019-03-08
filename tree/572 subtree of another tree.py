# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: 'TreeNode', t: 'TreeNode') -> 'bool':
        if not s and not t:
            return True
        if not s or not t:
            return False
        if self.compare(t,s):
            return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    def compare(self,a,b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return self.compare(a.left,b.left) and self.compare(a.right,b.right)


#  伪码
# int subtree(node *M, node *S)
#     先检查s/m为none的情况
#     if idential(m,s)
#         return True
#     subtree(M左 M右)