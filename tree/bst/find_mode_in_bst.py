# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        max_num = 1

        def helper(root):
            nonlocal max_num, ret
            if not root:
                return 0

            count = 1

            if not root.left and not root.right:
                return count

            # divide
            l_num = helper(root.left)
            r_num = helper(root.right)

            #conquer
            if root.left and root.left.val == root.val:
                count += l_num

            if root.right and root.right.val == root.val:
                count += r_num

            if count > max_num:
                max_num = count
                ret = [root.val]
            elif count == max_num:
                ret.append(root.val)

            return count

        helper(root)
        return ret
