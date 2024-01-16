class Solution:

    def meetingRoomIII(self, intervals, rooms, ask):
        # Write your code here.
        sum = [0 for i in range(50050)]
        vis = [0 for i in range(50050)]
        length = len(ask)
        ans = [False for i in range(length)]

        maxn = 0
        for i in range(0, len(intervals)):
            vis[intervals[i][0]] += 1
            vis[intervals[i][1]] -= 1
            maxn = max(maxn, intervals[i][1])

        tmp = 0
        for i in range(0, length):
            maxn = max(maxn, ask[i][1])

        for i in range(1, maxn + 1):
            tmp += vis[i]
            if tmp < rooms:
                sum[i] = 0
            else:
                sum[i] = 1

        for i in range(1, maxn + 1):
            sum[i] += sum[i - 1]
        for i in range(0, length):
            if sum[ask[i][0] - 1] == sum[ask[i][1] - 1]:
                ans[i] = True
            else:
                ans[i] = False
        return ans
