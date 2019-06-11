class Solution(object):

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return list()
        res = list()

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


# xidong's sol:
class Solution(object):

    def addOperators(self, num: str, target: int) -> List[str]:

        ret = list()

        def dfs(start, expression, val, prev):
            if start == len(num):
                if target == val:
                    ret.append(expression[:])
                return

            for i in range(start, len(num)):
                if num[start] == "0" and i > start:
                    return
                if start != 0:
                    dfs(i + 1, expression + "+" + num[start:i + 1], val + int(num[start:i + 1]), int(num[start:i + 1]))
                    dfs(i + 1, expression + "-" + num[start:i + 1], val - int(num[start:i + 1]), -int(num[start:i + 1]))
                    dfs(i + 1, expression + "*" + num[start:i + 1], (val - prev) + prev * int(num[start:i + 1]),
                        prev * int(num[start:i + 1]))
                else:
                    dfs(i + 1, expression + num[start:i + 1], int(num[start:i + 1]), int(num[start:i + 1]))

        dfs(0, "", 0, 0)
        return ret

