# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        ret = []

        def search_n_layer(root, layer, target):
            ret = []
            if root is None:
                return
            if layer == target:
                ret.append(root.val)
            for x in [root.left, root.right]:
                if x is not None:
                    search_n_layer(x, layer+1, target)

        def helper(root, t, K):

            nonlocal ret

            if root is None:
                return -1

            target = False
            dis = -1
            # divide
            l_has_target, l_dis = helper(root.left, t, K)
            r_has_target, r_dis = helper(root.right, t, K)

            # conquer
            if l_has_target or r_has_target or root.val == t:
                target = True
                if l_has_target:
                    dis = l_dis + 1
                elif r_has_target:
                    dis = r_dis + 1

                # search d = K-dis return == 0
                search_n_layer(root)

            return target, dis
