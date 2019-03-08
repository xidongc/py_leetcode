class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        list = [False for i in range(n)]
        for i in range(2,n):
            if list[i] == False:
                count += 1
                j = 2
                while j * i < n:
                    list[i*j] = True
                    j += 1
        return count

s = Solution()
print(s.countPrimes(20))