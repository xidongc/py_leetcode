from functools import cmp_to_key


class Solution(object):

    def valid(self, nums):

        def mycmp(num1, num2):
            for i in range(min(len(num1), len(num2))):
                if num1[i] > num2[i]:
                    return 1
                elif num1[i] < num2[i]:
                    return -1

            if len(num1) == len(num2):
                return 0
            else:
                return len(num1) < len(num2)

        val = sorted(nums, key=cmp_to_key(lambda x, y: mycmp(x, y)))
        return val == nums


s = Solution()
nums = ["a", "ab", "aa"]
print(s.valid(nums))
