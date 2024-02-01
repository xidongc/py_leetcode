class Solution(object):

    # with repeated ele, so select i ele only if i-1 is selected
    # if ele[i] == ele[i-1]
    def permuteUnique(self, nums):

        result = []
        nums.sort()

        def helper(tmp):
            nonlocal nums, result

            if len(tmp) == len(nums):
                result.append([nums[i] for i in tmp])
                return
            elif len(tmp) > len(nums):
                return

            for i in range(len(nums)):
                if i not in tmp:
                    if i > 0 and nums[i] == nums[i - 1] and i - 1 not in tmp:
                        continue

                    tmp.append(i)
                    helper(tmp)
                    tmp.pop()
