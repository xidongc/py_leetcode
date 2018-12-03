# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
# LC 117
# BFS

class Solution(object):
    # @param root, a tree link node
    # @return nothing

    def connect(self, root):
        ret = [-1 for _ in range(self.get_height(root))]

        def helper(root, level):
            if root is None:
                return

            if ret[level] != -1:
                ret[level].next = root
                ret[level] = root
            else:
                ret[level] = root

            helper(root.left, level+1)
            helper(root.right, level+1)

        helper(root, 0)

    def get_height(self, root):
        if root is None:
            return 0
        return max(self.get_height(root.left), self.get_height(root.right)) + 1

#lmf
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        cur = root
        while cur:
            leftMost = None
            prev = None
            while cur:
                # 每层prev, leftMost都要变鸭因为不然就向下一层指了
                if cur.left:
                    # 出现prev代表leftMost已经设置过了
                    if prev:
                        prev.next = cur.left
                    else:
                        leftMost = cur.left
                    prev = cur.left
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    else:
                        leftMost = cur.right
                    prev = cur.right
                cur = cur.next
            cur = leftMost
