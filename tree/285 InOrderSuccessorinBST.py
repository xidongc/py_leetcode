# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. root的值 =< p的值 答案就在右子树中
# 2. root的值 > p的值 答案有两个备选: a) 就是root
# b) 左子树中找(如果找到就一定是它，因为左子树的中的元素都比根小)
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        s = root
        res = None
        while s != None:
            if p.val < s.val:
                res = s
                s = s.left
            else:
                s = s.right
        return res

# https://www.youtube.com/watch?v=JdmAYw5h3G8
# case1: p has the right subtree(40), then search for its first right successor
# case2: p has not right subtree(37), 最近的向左走的root。 比如40
#               50
#           16      90
#       14     40
#     10  15  35  45
#            32 36
#                 37