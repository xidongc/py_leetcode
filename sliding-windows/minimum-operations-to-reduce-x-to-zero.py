def minOperations(self, nums, x: int) -> int:

    target = sum(nums) - x
    if target == 0:
        return len(nums)
    elif target < 0:
        return -1
    j, total, result = 0, 0, float("-inf")

    for i in range(len(nums)):
        while j < len(nums):
            if total + nums[j] < target:
                total += nums[j]
                j += 1
            elif total + nums[j] == target:
                total += nums[j]
                result = max(result, j - i + 1)
                j += 1
            else:
                break

        total -= nums[i]
    return len(nums) - result if result != float("-inf") else -1
