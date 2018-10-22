# 849 Maximize Distance to Closest Person
# https://leetcode.com/problems/maximize-distance-to-closest-person/description/


class Solution:

    # time complexity O(n)
    # two pointers

    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        dis = [0 for _ in range(len(seats))]
        if seats[0] == 1:
            p1 = p2 = 0
        else:
            t = 1
            while seats[t] != 1:
                t += 1
            for x in range(t):
                dis[x] = t - x
            p1 = p2 = t

        if seats[-1] == 1:
            p3 = len(seats) - 1
        else:
            t = len(seats) - 2
            while seats[t] != 1:
                t -= 1
            for x in range(len(seats) - t):
                dis[t+x] = x
            p3 = t

        while p1 != p3:
            if seats[p2] != 1:
                p2 += 1
            else:
                for j in range(1, (p2 - p1) // 2 + 1):
                    dis[p1+j] = j
                    dis[p2-j] = j
                p1 = p2
                p2 += 1

        print(dis)
        return max(dis)
