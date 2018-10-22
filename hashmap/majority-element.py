class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        ret = []
        hashmap = {}
        size = len(nums)
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        for x in hashmap:
            if hashmap[x] > size // 2:
                ret.append(x)
        return ret[0]