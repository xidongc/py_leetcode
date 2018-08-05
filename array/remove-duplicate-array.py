class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = 0
        for i in range(len(nums)):
            if nums[i] != nums[tmp]:
                nums[tmp+1] = nums[i]
                tmp += 1
        print(nums[0:tmp+1])
        return tmp+1

s = Solution()
print(s.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))

