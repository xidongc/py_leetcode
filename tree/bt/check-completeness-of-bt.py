class Solution(object):

    def isCompleteTree(self, root):

        """
        :type root: TreeNode
        :rtype: bool
        """

        nodes = [(root, 1)]
        i = 0

        while i < len(nodes):
            (curr, index) = nodes[i]
            i += 1
            if curr.left:
                nodes.append((curr.left, index * 2))
            if curr.right:
                nodes.append((curr.right, index * 2 + 1))
        return nodes[-1][1] == len(nodes)
