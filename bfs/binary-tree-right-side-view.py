import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        q = queue.Queue()
        result = []
        q.put(root)
        while not q.empty():
            level = []
            size = q.qsize()
            for _ in range(size):
                node = q.get()
                level.append(node.val)
                for x in [node.left, node.right]:
                    if x is not None:
                        q.put(x)
            result.append(level[:][-1])
        return result