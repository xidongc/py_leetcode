from tree import TreeNode


# recursive
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


# iterative, post order need two stacks
class Solution(object):

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return list()

        output = list()
        stack1 = list()
        stack2 = list()

        stack1.append(root)

        while len(stack1) > 0:
            curr = stack1.pop()
            if curr.left:
                stack1.append(curr.left)
            if curr.right:
                stack1.append(curr.right)
            stack2.append(curr)

        while len(stack2) > 0:
            output.append(stack2.pop().val)

        return output
