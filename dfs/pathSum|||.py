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

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
        
