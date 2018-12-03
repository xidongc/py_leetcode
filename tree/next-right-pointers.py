# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
# LC 116
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

# lmf
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        cur = root
        leftMost = cur.left
        while leftMost:
            while cur:
                cur.left.next = cur.right
                # cur.next为空的node的right.next为空
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            cur = leftMost
            leftMost = cur.left


# 只有right的next会指向none，所以左边就直接加指针