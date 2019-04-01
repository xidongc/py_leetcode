from tree.TreeNode import TreeNode


class Solution(object):

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0 or len(postorder) != len(inorder):
            return None

        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[0:root_index], postorder[0:root_index])
        root.right = self.buildTree(inorder[root_index + 1:], postorder[root_index: len(postorder) - 1])
        return root

