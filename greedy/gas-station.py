class Solution:
    def canCompleteCircuit(self, gas, cost):

        ret = -1
        sum = total = 0
        k = 0
        comb = [gas[i] - cost[i] for i in range(len(gas))]

        for i in range(len(gas)):
            sum += comb[i]
            if sum < 0:
                sum = 0
                k = i+1
            total += comb[i]
        if total < 0:
            return ret

        return k
