class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [1,1,1,2,2,3]

        p1 = 0
        p2 = 0

        target = -1
        repeat = 0

        for num in nums:
            if num == target:
                repeat += 1
            else:
                target = num
                repeat = 1

            if repeat <= 2:
                nums[p2] = num
                p1 += 1
                p2 += 1
            else:
                p1 += 1

        print(nums[0:p2])

        return p2


nums = [1,1,1,2,2,3]
s = Solution()
s.removeDuplicates(nums)