def jumps(array):
    start = 0
    cur = array[0] + 1
    if array[0] >= n:
        return 1
    times = 0
    dp = [-1] * n
    for j in range(cur):
        dp[j] = 1
    for i in range(cur, n):
        for j in range(0,i):
            if dp[j] > 0 and j + array[j] >= i:
                dp[i] = min(dp[j] + 1,dp[i]) if dp[i] > 0 else dp[j] + 1
    return dp[-1]


n = int(input())
array = [int(x) for x in input().split()]

print(jumps(array))

# jumps([3,2,1,0,0]) = 0