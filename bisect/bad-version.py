# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n

        if n < 1:
            return None

        while start < end - 1:
            mid = (end - start)/2 + start
            if isBadVersion(mid) is False:
                start = mid
            elif isBadVersion(mid) is True:
                end = mid
            else:
                return

        if isBadVersion(start) is True:
            return start

        if isBadVersion(end) is True:
            return end

        return None
# lmf
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left + 1 < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left if isBadVersion(left) else right


