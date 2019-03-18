from tree import TreeNode


class Solution(object):

    # recursive
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = list()
        if not root:
            return ret

        def helper(root):
            if root is None:
                return

            helper(root.left)
            ret.append(root.val)
            helper(root.right)

        helper(root)
        return ret
