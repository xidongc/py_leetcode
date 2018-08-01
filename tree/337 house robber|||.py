#DFS
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
# #1
#     def rob(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         Solution.res1 = 0
#         Solution.res2 = 0
#         self.helper(root,1)
#         return max(Solution.res1,Solution.res2)
#
#     def helper(self,root,level):
#         if not root:
#             return
#         if level%2 == 0:
#             Solution.res2 += root.val
#         else:
#             Solution.res1 += root.val
#         self.helper(root.left,level+1)
#         self.helper(root.right,level+1)
# #2
#     def rob(self, root):
#         def dfs(root):
#             if not root : return [0, 0]
#             robLeft = dfs(root.left)
#             robRight = dfs(root.right)
#             return [robLeft[1]+robRight[1]+root.val, robLeft[0]+robRight[0]]
#         return max(dfs(root)[0],dfs(root)[1])
# #有个case ac不了我也不知道为什么
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root):
            res = [0  # Current level max value
                , 0]  # Lower level max value
            if root:
                left = helper(root.left)
                right = helper(root.right)
                res[1] = left[0] + right[0]  # root下一层的和
                res[0] = max(res[1], left[1] + right[1] + root.val)  # left[1],right[1] root下两层
                # print(res)
            return res

        return helper(root)[0]
root = TreeNode(3)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.right = TreeNode(3)
root.right.right = TreeNode(1)
s = Solution()
s.rob(root)