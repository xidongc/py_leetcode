class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        ret = -1
        sum = total = 0
        k = 0
        comb = [gas[i] - cost[i] for i in range(len(gas))]
        print(comb)


        for i in range(len(gas)):
            sum += comb[i]
            if sum < 0:
                sum = 0
                k = i+1
            total += comb[i]
        if total < 0:
            return ret

        return k

gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
s = Solution()
print(s.canCompleteCircuit(gas, cost))