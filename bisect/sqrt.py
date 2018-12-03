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

    # 对小数也有处理的case
    def sqrt(self,x):
        if x >= 1:
            start,end = 1,x
        else:
            start,end = x,1
        #     almost no differce?
        while end - start > 1e-10:
            mid = (start+end)/2
            if mid * mid < x:
                start = mid
            else:
                end = mid
        return round(start,2)
s = Solution()
print(s.sqrt(1/4))
print(s.sqrt(4))
