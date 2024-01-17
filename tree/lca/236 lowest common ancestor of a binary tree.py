# 小笔记p18
# 1. bottom up 最优
# 2. 公共路经法
# 3. top down，对root左右节点调用hasnode看p，q是在左还是在右，else return root



class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # solution with no parent

        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if not left and not right:
            return None
        return left if left else right

    def lowestCommonAncestorII(self, root, A, B):
        # solution with parent node
        visited = set()
        while A is not root:
            visited.add(A)
            A = A.parent

        while B is not root:
            if B in visited:
                return B
            B = B.parent
