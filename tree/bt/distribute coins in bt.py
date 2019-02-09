class Solution(object):

    def distributeCoins(self, root: 'TreeNode') -> 'int':

        def helper(root):
            if root is None:
                return (0,0)
            if root.left is None and root.right is None:
                return abs(root.val - 1), root.val - 1
            step_left = helper(root.left)
            step_right = helper(root.right)
            val = step_left[1]+step_right[1]+root.val-1
            step = abs(step_left[0]) + abs(step_right[0]) + abs(val)
            return step, val

        return helper(root)[0]
