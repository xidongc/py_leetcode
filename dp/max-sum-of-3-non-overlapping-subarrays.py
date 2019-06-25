# sol refer to https://blog.csdn.net/fuxuemingzhu/article/details/82947707
# but more concise in indexing

class Solution(object):

    def maxSumOfThreeSubarrays(self, nums, k):

        # corner case
        if len(nums) < 3*k:
            return list()

        n = len(nums)
        left = [0 for _ in range(n)] # left array
        right = [n - k for _ in range(n)] # right array
        presum = [0] # presum array

        # calculate presum
        total = 0
        for i in range(n):
            total += nums[i]
            presum.append(total)

        # calculate left
        total = presum[k] - presum[0]
        for i in range(1, n - k + 1):
            if presum[i + k] - presum[i] > total:
                total = presum[i + k] - presum[i]
                left[i] = i
            else:
                left[i] = left[i - 1]

        # calculate right
        total = presum[n] - presum[n - k]
        for i in range(n - 1, k - 1, -1):
            if presum[i] - presum[i - k] > total:
                total = presum[i] - presum[i - k]
                right[i - k] = i - k
            else:
                right[i - k] = right[i - k + 1]

        # calculate three as a whole
        total = float("-inf")
        res = [0, 0, 0]

        for j in range(k, n-2*k+1):
            l = left[j - k]
            r = right[j + k]
            if presum[l + k] - presum[l] + presum[j + k] - presum[j] + presum[r + k] - presum[r] > total:
                total = presum[l + k] - presum[l] + presum[j + k] - presum[j] + presum[r + k] - presum[r]
                res = [l, j, r]

        return res
