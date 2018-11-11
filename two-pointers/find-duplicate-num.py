class Solution(object):

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        [1,3,4,2,2]
        nums.sort()

        for i, num in enumerate(nums):
            if nums[i] == nums[i-1]:
                return nums[i]

        return None
# linked list cycle|| 必有下标环

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast