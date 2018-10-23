class Solution:
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

