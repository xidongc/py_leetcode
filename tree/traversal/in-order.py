from tree import TreeNode


class Solution(object):

    # recursive
    def inorderTraversal(self, root):

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

    # iterative
    def inorderTraversal_II(self, root: TreeNode):
        if not root:
            return list()

        stack = list()
        output = list()
        curr = root

        while curr:
            stack.append(curr)
            curr = curr.left

        while len(stack) > 0:
            curr = stack.pop()
            output.append(curr.val)
            curr = curr.right
            while curr:
                stack.append(curr)
                curr = curr.left

        return output
