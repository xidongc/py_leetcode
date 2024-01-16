# sol-1 recursion
class Solution(object):

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(nums):
            if not nums or len(nums) == 0:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            x = max(nums)
            index = nums.index(x)
            root = TreeNode(x)
            root.left = helper(nums[0:index])
            root.right = helper(nums[index+1:])
            return root

        root = helper(nums)
        return root

# sol-2 monotone stack
class Solution(object):

    def constructMaximumBinaryTree(self, nums):
        mono_stack = []
        left = [float("inf")] * len(nums)
        right = [float("inf")] * len(nums)
        tree = [TreeNode(num) for num in nums]

        for i in range(len(nums)):
            while mono_stack and nums[mono_stack[-1]] < nums[i]:
                right[mono_stack.pop()] = i
            left[i] = mono_stack[-1] if mono_stack else float("inf")
            mono_stack.append(i)

        root = None
        for i in range(len(nums)):
            if left[i] == float("inf") and right[i] == float("inf"):
                root = tree[i]
            elif right[i] == float("inf"):
                tree[left[i]].right = tree[i]
            elif left[i] == float("inf"):
                tree[right[i]].left = tree[i]
            elif nums[left[i]] < nums[right[i]]:
                tree[left[i]].right = tree[i]
            else:
                tree[right[i]].left = tree[i]
        return root
