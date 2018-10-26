class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Solution.res = []
        def backtrack(nums,tmpList,pos):
            Solution.res.append(tmpList)
            for i in range(pos,len(nums)):
                backtrack(nums,tmpList+[nums[i]],i+1)
        backtrack(nums,[],0)
        return Solution.res