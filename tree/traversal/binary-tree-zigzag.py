# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = [[] for _ in range(self.getHeight(root))]
        self.dfs(root, 0, ret)
        for i, num in enumerate(ret):
            if i%2==1:
                ret[i].reverse()
        return ret

    def getHeight(self, root):
        if root is None:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        return max(left, right) + 1

    def dfs(self, root, level, ret):
        if root is None:
            return
        ret[level].append(root.val)
        self.dfs(root.left, level+1, ret)
        self.dfs(root.right, level+1, ret)

# Sol-2: bfs level traversal

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        queue = list()
        queue.append(root)
        level = 0

        ret = [[root.val]]

        while len(queue) > 0:
            length = len(queue)
            tmp = []
            for i in range(length):
                ele = queue.pop(0)
                for x in [ele.left, ele.right]:
                    if x is not None:
                        queue.append(x)
                        tmp.append(x.val)
            level += 1
            if level % 2 == 1:
                tmp.reverse()
            if len(tmp) > 0:
                ret.append(tmp)
        return ret
