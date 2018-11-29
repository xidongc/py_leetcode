class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or sum(nums) % k:
            return False
        visited = [False] * len(nums)
        def helper(nums,k,start,target,visited,tmpSum):
            if k == 1:
                return True
            if tmpSum == target:
                return helper(nums,k-1,0,target,visited,0)
            if tmpSum < target:
                for i in range(start,len(nums)):
                    if visited[i] or tmpSum > target:
                        continue
                    visited[i] = True
                    if helper(nums,k,i+1,target,visited,tmpSum + nums[i]):
                        return True
                    visited[i] = False
            return False
        return helper(nums,k,0,sum(nums) // k,visited,0)
s = Solution()
s.canPartitionKSubsets([1,1,1,1,1,1,1,1,1,1],5)
