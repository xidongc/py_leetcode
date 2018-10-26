class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        # the start should be 0 since no one's sqrt is 0 except for 0
        start = 1
        end = x

        while start < end -1:
            mid = (end - start)/2 + start
            if mid ** 2 > x:
                end = mid
            elif mid ** 2 < x:
                start = mid
            else:
                return mid

        return start