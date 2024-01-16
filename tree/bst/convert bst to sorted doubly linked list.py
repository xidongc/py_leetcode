"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution(object):

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        dummy = Node(0, None, None)
        dummy.right = root
        curr = dummy

        def helper(root):
            nonlocal curr
            if root is None:
                return

            helper(root.left)
            curr.right = root
            root.left = curr
            curr = root
            helper(root.right)

        helper(root)
        curr.right = dummy.right
        dummy.right.lef`t = curr
        return dummy.right
