# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
#
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return -1
        res =
        # Find potential celebrity
        for i in range(1, n):
            if knows(res, i):
                res = i
        # if celebrity knows someone / someone does not knoe celebrity
        # then no celebrity in this array
        for i in range(n):
            if i != res and knows(i, res) == False:
                return -1
            if i != res and knows(res, i):
                return -1
        return res
