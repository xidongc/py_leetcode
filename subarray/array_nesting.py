class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return []
        visited = [False] * len(nums)
        res = 0
        for i in range(len(nums)):
            temp = 0
            while not visited[i]:
                temp += 1
                visited[i] = True
                i = nums[i]
            res = max(res,temp)
        return res
