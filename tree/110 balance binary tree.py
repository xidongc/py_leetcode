class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # corner case
        if not root:
            return True

        def helper(root):
            if not root:
                return 0, True
            left, con1 = helper(root.left)
            right, con2 = helper(root.right)
            con3 = False
            if -1 <= left - right <= 1:
                con3 = True
            # multiple return val
            return max(left, right) + 1, con1 and con2 and con3

        return helper(root)[1]
