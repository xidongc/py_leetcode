# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = postorder[-1]
        left_tree_in = inorder[0: inorder.index(root)]
        left_tree_post = postorder[0:len(left_tree_in)]
        
        right_tree_in = inorder[inorder.index(root) + 1:len(inorder)]
        right_tree_post = postorder[-len(right_tree_in)-1:-1]
        root = TreeNode(postorder[-1])
        root.left = self.buildTree(left_tree_in, left_tree_post)
        root.right = self.buildTree(right_tree_in, right_tree_post)
        return root

class Solution(object):
    def buildTree(self,  inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root = TreeNode(postorder.pop())
            inPos = inorder.index(root.val)
            root.right = self.buildTree(inorder[inPos + 1:],postorder)
            root.left = self.buildTree(inorder[:inPos],postorder)
            return root
