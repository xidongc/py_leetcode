# inList = []
# for _ in range(3):
#     inList.append(input())
# target = int(inList[2])
# nums = list(map(int, list(inList[1].split(' '))))
# print(target)
# print(nums)


# candidates.sort()
# dp = [[[]]] + [[] for i in xrange(target)]
# for i in xrange(1, target + 1):
#     for number in candidates:
#         if number > i: break
#         for L in dp[i - number]:
#             if not L or number >= L[-1]: dp[i] += L + [number],
# return dp[target]

#
# def numberOfWays(target):
#   x = target[0]
#   y = target[1]
#   dp = [[0 for _ in range(x+1)] for _ in range(x+1)]
#   dp[0][0] = 0
#   dp[1][0] = 1
#   dp[1][1] = 1
#   dp[1][-1] = 1
#   dp[0][1] = 0
#   dp[0][-1] = 0
#   inList = [[0,0],[1,0],[1,1],[1,-1],[0,1],[0,-1]]
#
#   for i in range(1, x+1):
#     for j in range(0, x+1):
#       if (i,j) not in inList:
#         dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j+1]
#   return dp[x][y]
# s = []
# def helper(tmp,pos):
#   if pos == 4:
#       a = tmp[:]
#       print(a)
#       s.append(a)
#       print(s)
#       return
#   for i in range(pos):
#     # tmp.append(i)
#       helper(tmp+[i],pos + 1)
#     # tmp.remove(i)
# # print(s)
#
# helper([],1)

import collections
print(collections.Counter(['a','b','b','c','c','c']))
print(dict(collections.Counter('abbccced')))
dict = {'a':2,'b':1,'t':5,'e':2}
print(list(dict.keys()))
print(list(dict.values()))
list = ['a','b','b','c','d','c']
list.sort(key=lambda x: ord(x))
print(list)

# print(numberOfWays([2,1]))
