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
        if not root or not p:
            return None
        # 因为是比它大的，所以肯定要走到左子树鸭
        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            if left == None:
                return root
            else:
                return left

# ?????????????????????????????????????????????????/