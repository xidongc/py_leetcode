
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow, fast = n,n
        while 1:
            slow = self.countSum(slow)
            fast = self.countSum(fast)
            fast = self.countSum(fast)
            if slow == fast:
                break
        if slow == 1:
            return True
        else:
            return False
    def countSum(self, num):
        sum = 0
        while num:
            temp = num % 10
            sum += temp * temp
            num = num//10
        return sum
# 快指针一直走两步，慢指针走一步，如果有环，在环这里二者距离每次缩小1，总能追上。所以若是s==f就说明有环。
s = Solution()
print(s.isHappy(19))
# lc 141
# There must be a cycle. at most 200