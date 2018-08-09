# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root = TreeNode(preorder.pop(0))
            inPos = inorder.index(root.val)
            # preorder changed while backtracking, so the the following two preorders are different
            root.left = self.buildTree(preorder,inorder[:inPos])
            root.right = self.buildTree(preorder,inorder[inPos+1:])
            return root
#        else no return = None