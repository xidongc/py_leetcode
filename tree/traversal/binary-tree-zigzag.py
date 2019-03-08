class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # bfs level traversal

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
