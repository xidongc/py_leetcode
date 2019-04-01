class Solution:

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # bfs

        # corner case
        if root is None:
            return 0

        queue = list()
        queue.append((root, 0))
        level = 1

        while len(queue) > 0:
            length = len(queue)
            tmp = list()
            for _ in range(length):
                curr, x = queue.pop(0)
                tmp.append(x)

                if curr.left:
                    queue.append((curr.left, 2*x))
                if curr.right:
                    queue.append((curr.right, 2*x+1))

            level = max(level, max(tmp)-min(tmp)+1)
        return level


