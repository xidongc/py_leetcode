class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        res = []

        def dfs(target, num, start, string, tmpSum, lastf):
            if start == len(num):
                if tmpSum == target:
                    res.append(string)
                return
            for i in range(start, len(num)):
                x = int(num[start:i + 1])
                #                 Start number has no leading operator
                if start == 0:
                    dfs(target, num, i + 1, '' + str(x), x, x)
                else:
                    dfs(target, num, i + 1, string + '+' + str(x), tmpSum + x, x)
                    dfs(target, num, i + 1, string + '-' + str(x), tmpSum - x, -x)
                    dfs(target, num, i + 1, string + '*' + str(x), tmpSum - lastf + lastf * x, lastf * x)
                # no leading 0 or duplicate 0.
                # if there is leading 0, then only allows the situation where only one 0
                # counted in the recursion, loop stops here.
                if x == 0:
                    break

        dfs(target, num, 0, '', 0, 0)
        return res

