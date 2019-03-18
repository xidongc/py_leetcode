from tree import TreeNode


class Solution(object):

    def postorderTraversal(self, root):
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
            helper(root.right)
            ret.append(root.val)

        helper(root)
        return ret
