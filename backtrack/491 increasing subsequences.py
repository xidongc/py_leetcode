# To write a tuple containing a single value you have to include a comma,
# even though there is only one value (a,)
# set: {} dict : {}
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #
        # Solution.res = []
        #
        # def dfs(nums, start, tempList):
        #     if len(tempList) >= 2:
        #         Solution.res.append(tempList)
        #     for i in range(start, len(nums)):
        #         if not tempList or nums[i] >= tempList[-1]:
        #             dfs(nums, i + 1, tempList + [nums[i]])
        # dfs(nums, 0, [])
        # return Solution.res
#         Stefan大佬的做法
        res = {()}
        for num in nums:
            # res |= performs the union operation of two python sets
            res |= { sub + (num,)
                    for sub in res
                    if not sub or num >= sub[-1]}
        #     tuple of list 作为list of list 并没有什么问题　?
        return [sub for sub in res if len(sub) >= 2]
s = Solution()
print(s.findSubsequences([1,2,3,4]))
