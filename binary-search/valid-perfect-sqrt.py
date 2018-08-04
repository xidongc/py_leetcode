class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        if x == 0 or x == 1:
            return True
        start = 1
        end = x

        while start < end -1:
            mid = (end - start)/2 + start
            if mid ** 2 > x:
                end = mid
            elif mid ** 2 < x:
                start = mid
            else:
                return True

        return False