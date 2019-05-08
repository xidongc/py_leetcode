# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(min, max, node):
            if node is None:
                return True
            con1 = (min < node.val < max)
            con2 = helper(min, node.val, node.left)
            con3 = helper(node.val, max, node.right)
            return con1 and con2 and con3

        return helper(float("-inf"), float("inf"), root)


# lmf
# 中序遍历，1）可以用数组
#          2）省去数组，用prev记录前一个，因为是严格升序所以右子树最左子肯定比node大
class Solution(object):

    def isValidBST(self, root):
        Solution.prev = None

        def helper(root):
            if not root:
                return True
            if not helper(root.left):
                return False
            if Solution.prev and Solution.prev >= root.val:
                return False
            Solution.prev = root.val
            return helper(root.right)
        return helper(root)


# in order traversal with iterative
class Solution(object):

    def isValidBST(self, root: TreeNode) -> bool:

        # corner case
        if not root:
            return True

        stack = list()
        curr = root
        prev = float("-inf")

        while curr:
            stack.append(curr)
            curr = curr.left

        while len(stack) > 0:
            node = stack.pop()
            if node.val <= prev:
                return False
            prev = node.val
            curr = node.right
            while curr:
                stack.append(curr)
                curr = curr.left
        return True
