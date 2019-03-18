from tree import TreeNode


class Solution(object):

    def preorderTraversal(self, root):
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
            ret.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        return ret
