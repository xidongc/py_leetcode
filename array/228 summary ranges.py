class Solution:
    def summaryRanges(self, nums: 'List[int]') -> 'List[str]':
        if not nums:
            return []
        res = []
        s,e = nums[0],2**32-1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                e = nums[i-1]
                if s == e:
                    res.append(str(s))
                else:
                    res.append(str(s) + '->' + str(e))
                s = nums[i]
        if s == nums[-1]:
            res.append(str(s))
        else:
            res.append(str(s) + '->' + str(nums[-1]))
        return res
s = Solution()
s.summaryRanges([0,1,2,4,5,7])
