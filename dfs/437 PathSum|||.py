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
        :rtype: int
        """
        if not root:
            return 0
        return self.pathFromSum(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    def pathFromSum(self, root, sum):
        if not root:
            return 0
        return (1 if root.val == sum else 0) + self.pathFromSum(root.left, sum - root.val) + self.pathFromSum(root.right, sum - root.val)

# 每层sum遍历就不停的调用left和right的主函数
# 同时需要有一个从root到下的计算sum方法
# 因为可能有val为负的node，故即使sum==val也要向下遍历