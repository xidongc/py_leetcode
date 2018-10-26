#
# Complete the 'climbTheHill' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY slope as parameter.
#

def climbTheHill(slopes):
    # Write your code here
    length = len(slopes)
    dp = [0]*length
    tmpList = [0]*length
    res = 2 ** 32 - 1
    for i in range(length):
        tmpList[i] = slopes[i]
    tmpList.sort()
    for i in range(length):
        tmp = 2 ** 32 - 1
        for j in range(length):
            tmp = min(tmp,dp[j])
            dp[j] = abs(tmpList[j]-slopes[i]) + tmp
    for i in range(length):
        res = min(dp[i],res)
    return res
print(climbTheHill([9,8,7,3,3,3]))