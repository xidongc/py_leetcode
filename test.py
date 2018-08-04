zero = 0
nums = [1,0,1,0,4]
for i in range(len(nums)):
    if not nums[i] == 0 and zero <= i:
        nums[i], nums[zero] = nums[zero], nums[i]
        zero += 1