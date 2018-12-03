# import sys
# num, length = input().strip().split(' ')
# length = int(length)
# s = input()
# minList = [0]*26
length = 4
dp = [[0 for _ in range(length)] for _ in range(length)]
# count = 0
# for line in sys.stdin:
#     c,add,dele = line.strip().split(' ')
#     minList[ord(c)-ord('a')] = min(add,dele)
#     count += 1
#     if count == int(num):
#         break

s = 'abcb'
minList = ['1000', '350', '200', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(length-1,-1,-1):
    for j in range(i+1,length):
        # 首先：对于一个串如果s【i】==s【j】，那么dp【i】【j】=dp【i+1】【j-1】
        #
        # 其次：如果dp【i+1】【j】是回文串，那么dp【i】【j】=dp【i+1】【j】+min（add【i】，del【i】）；
        #
        # 最后，如果dp【i】【j-1】是回文串，那么dp【i】【j】=dp【i】【j-1】 + min（add【j】，del【j】）
        dp[i][j] = min(dp[i+1][j] + int(minList[ord(s[i])-ord('a')]),dp[i][j-1] + int(minList[ord(s[j])-ord('a')]))
        if s[i] == s[j]:
            dp[i][j] = min(dp[i][j],dp[i+1][j-1])
print(dp[0][length-1])
# 区间dp,从基础2个点开始，从基础情况开始每个区间记录能达到回文的最小cost
# 如果遇到回文串就比较一下哪种cost小（因为中心选取的不同

