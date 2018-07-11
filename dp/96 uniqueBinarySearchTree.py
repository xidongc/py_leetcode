class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0 for i in range(n+1)]
        res[0] = 1
        res[1] = 1
        for i in range(2,n+1):
            for j in range(1,i+1):
                res[i] += res[j-1]*res[i-j]
        return res[n]
        # G(0) = 1, G(1) = 1,
        # 左为0（1） 2右为1 i=2，j=1，2
        # G(2) = G(1)*G(0) + G(0)G(1)
