class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums or len(nums) == 0:
            return nums
        row = len(nums)
        col = len(nums[0])
        if row*col != r*c:
            return nums
        res = []
        for i in range(row):
            for j in range(col):
                res.append(nums[i][j])
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(res[0])
                res.pop(0)
            res.append(temp)
        return res
                
