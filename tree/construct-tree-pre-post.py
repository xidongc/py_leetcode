# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        hash_in = {}
        for i, num in enumerate(inorder):
            hash_in[num] = i

        return self.find_tree_root(preorder, 0, len(preorder), inorder, 0, len(inorder), hash_in)

    #[si, ei)
    def find_tree_root(self, preorder, s0, e0, inorder, s1, e1, hash_in):
        if s0 >= e0 or s1 >= e1:
            return None
        index = hash_in.get(preorder[s0])
        root = TreeNode(preorder[s0])
        index = hash_in.get(preorder[s0])
        root.left = self.find_tree_root(preorder, s0+1, s0+1+index-s1, inorder, s1, index, hash_in)
        root.right = self.find_tree_root(preorder, s0+1+index-s1, e0, inorder, index+1, e1, hash_in)
        return root