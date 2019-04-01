class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        ret = list()

        # corner case
        if root is None:
            return ret

        queue = list()  # deque in python
        queue.append(root)
        level = 1

        while len(queue) > 0:
            length = len(queue)
            reverselist = list()
            for _ in range(length):
                tmp = queue.pop(0)
                for x in [tmp.left, tmp.right]:
                    if x:
                        queue.append(x)
                if level % 2 == 1:
                    reverselist.append(tmp.val)
                else:
                    reverselist.insert(0, tmp.val)

            ret.append(reverselist[:])
            level += 1

        return ret
