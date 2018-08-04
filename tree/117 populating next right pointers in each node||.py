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
