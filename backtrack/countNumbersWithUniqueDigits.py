# Following the hint. Let f(n) = count of number with unique digits of length n.
#
# f(1) = 10. (0, 1, 2, 3, ...., 9)
#
# f(2) = 9 * 9. Because for each number i from 1, ..., 9, we can pick j to form a 2-digit number ij and there are 9 numbers that are different from i for j to choose from.
#
# f(3) = f(2) * 8 = 9 * 9 * 8. Because for each number with unique digits of length 2, say ij, we can pick k to form a 3 digit number ijk and there are 8 numbers that are different from i and j for k to choose from.
#
# Similarly f(4) = f(3) * 7 = 9 * 9 * 8 * 7....
#
# ...
#
# f(10) = 9 * 9 * 8 * 7 * 6 * ... * 1
#
# f(11) = 0 = f(12) = f(13)....
#
# any number with length > 10 couldn't be unique digits number.
#
# The problem is asking for numbers from 0 to 10^n. Hence return f(1) + f(2) + .. + f(n)
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 1
        
        res = 10
        intRemain = 9
        intAvail = 9
        while n > 1 and intRemain > 0:
            intAvail = intAvail * intRemain
            res += intAvail
            intRemain -= 1
            n -= 1
        return res
