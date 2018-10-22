# Complete the getMinimumUniqueSum function below.
# 有一组有重复的数字，将重复数字增加到不重复，并且使和最小
def getMinimumUniqueSum(arr):
    arr.sort()
    sum = arr[0]
    for i in range(1,len(arr)):
        if arr[i] <= arr[i-1]:
            arr[i] = arr[i-1] + 1
        sum += arr[i]
    return sum
# 2,2,2,2
# 1,2,3,3,4