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
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        mono = []
        if len(nums) <= 0:
            return None

        for num in nums:
            tmp_list = []
            while len(mono) > 0 and mono[-1].val < num:
                tmp_list.append(mono.pop())
            node = TreeNode(num)
            mono.append(node)
            if len(tmp_list) > 0:
                node.left = tmp_list.pop()
                node = node.left
                while len(tmp_list) > 0:
                    node.right = tmp_list.pop()
                    node = node.right

        head = mono[0]
        curr = mono.pop()
        while len(mono) > 0:
            tmp = mono.pop()
            tmp.right = curr
            curr = tmp

        return head

