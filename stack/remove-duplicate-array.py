class Solution(object):
    # nktdcxd
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
#     nktdlmf
#     简单粗暴想法是pop(index)
    def removeDuplicates(self, nums):
        pointer = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[pointer]:
                pointer += 1
                nums[pointer] = nums[i]
        return pointer + 1
s = Solution()
print(s.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))

