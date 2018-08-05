class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        if not houses or not heaters:
            return -1
        heaters.sort()
        res = 0
        i = 0
        for house in sorted(houses):
            while i < len(heaters) - 1 and 2 * house >= heaters[i] + heaters[i+1]:
                i += 1
            res = max(res,abs(house - heaters[i]))
        return res

# while heaters[i] + heaters[i+1] <= 2 * x 代表i+1个heater离x最近，就找最近的那个heater。
# houses :        2____5
# heater:                    8 右边界
# heater:       1       左边界
# heater:           3
# 2,147,483,647.
# s = Solution()
# print(s.findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],
# [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]))
# sorted(a) 不改变a,a.sort()改变a
