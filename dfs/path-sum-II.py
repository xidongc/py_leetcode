# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        ret = []

        if not root:
            return ret

        curr = [root.val]

        def dfs(root, sum):
            if sum == 0 and root.left is None and root.right is None:
                print(curr)
                ret.append(curr[:])
            for n in [root.left, root.right]:
                if n is not None:
                    curr.append(n.val)
                    dfs(n, sum-n.val)
                    curr.pop()

        dfs(root, sum-root.val)
        return ret

class Solution:
     def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        Solution.res = []
        def helper(root, sum, path):
            if not root.left and not root.right and sum == root.val:
                Solution.res.append(path+[root.val])
                return
            helper(root.left, sum-root.val, path+[root.val])
            helper(root.right, sum-root.val, path+[root.val])
        helper(root,sum,[])
        return Solution.res