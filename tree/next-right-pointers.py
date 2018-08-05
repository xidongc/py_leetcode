# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# Solution 1:


class Solution(object):
    # @param root, a tree link node
    # @return nothing

    def connect(self, root):
        if root is None:
            return

        first = None
        p = root

        while p is not None:
            if first is None:
                first = p.left
            if p.left:
                p.left.next = p.right
            if p.right:
                if p.next:
                    p.right.next = p.next.left
                    p = p.next
                else:
                    p = first
                    first = None
            else:
                break


# Solution 2:

class Solution(object):
    # @param root, a tree link node
    # @return nothing

    def connect(self, root):
        if root is None:
            return

        first = None
        p = root

        while p is not None:
            if first is None:
                first = p.left
            if p.left:
                p.left.next = p.right
            elif p.right:
                if p.next:
                    p.right.next = p.next.left
                    p = p.next
                else:
                    p = first
                    first = None