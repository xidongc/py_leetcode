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

# lmf 
# 非递归
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            res.append(queue[-1].val)
            length = len(queue)
            for i in range(length):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res
# 递归
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        def dfs(root,level):
            if not root:
                return
            if level == len(res):
                res.append(root.val)
            dfs(root.right,level + 1)
            dfs(root.left,level + 1)
        dfs(root,0)
        return res