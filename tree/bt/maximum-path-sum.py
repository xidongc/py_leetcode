def max_path_sum(self, root) -> int:

    max_result = float("-inf")

    def helper(root):
        nonlocal max_result

        if not root:
            return 0, float("-inf")

        leftL, maxLH = helper(root.left)
        rightR, maxRH = helper(root.right)

        max_result = max(max_result, max(leftL + root.val, rightR + root.val, leftL + rightR + root.val, root.val))

        return max(max(leftL, rightR) + root.val, root.val), max(leftL + root.val, rightR + root.val,
                                                                 leftL + rightR + root.val, root.val)

    helper(root)
    return max_result
