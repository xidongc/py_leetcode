nums = [1,3,4,9,3,6,6,6]
target = 12
numset = set(nums)
res = 0
half = target // 2 if target % 2 == 0 else target / 2
if nums.count(half) > 1:
    res += 1
for num in nums:
    if target - num != half and (target - num) in numset:
        res += 1
        numset.remove(num)
print(res)