class Solution:

    def subsetsWithDup(self, nums):
        nums.sort()
        results = []

        def helper(start, tmp):
            nonlocal results ,nums
            results.append([nums[i] for i in tmp[:]])

            for i in range(start, len(nums)):
                if i not in tmp:
                    if i > 0 and i-1 not in tmp and nums[i-1] == nums[i]:
                        continue
                    else:
                        tmp.append(i)
                        helper(i+1, tmp)
                        tmp.pop()

        helper(0, [])
        return results
