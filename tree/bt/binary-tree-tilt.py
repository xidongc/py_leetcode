# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        def getSum(node):
            nonlocal sum
            if node is None:
                return 0, 0

            # divide
            lsum, lm = getSum(node.left)
            rsum, rm = getSum(node.right)

            # traverse
            sum += abs(lsum - rsum)

            #conquer
            return lsum + rsum + node.val, abs(lsum - rsum)

        getSum(root)
        return sum