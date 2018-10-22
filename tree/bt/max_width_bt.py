class Solution:

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = []
        q.append(root)
        ret = []
        while len(q) > 0:
            level = []
            size = len(q)
            for _ in range(size):
                val = q.pop(0)
                level.append(val.val)
                for i in [val.left, val.right]:
                    if i.left is not None and i.right is not None:
                        q.append(i)
            ret.append(level[:])
        print(ret)


