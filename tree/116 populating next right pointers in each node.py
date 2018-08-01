#BFS
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

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