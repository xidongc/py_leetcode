class Solution(object):

    def countAndSay(self, n: int) -> str:
        if n <= 0:
            return "0"
        elif n == 1:
            return "1"

        lastResult = self.countAndSay(n - 1)
        result = list(map(int, list(lastResult)))
        nextResult = list()

        curr = result[0]
        count = 1

        for i in range(1, len(result)):
            if result[i] == result[i-1]:
                count += 1
            elif result[i] != result[i-1]:
                nextResult.append((count, curr))
                curr = result[i]
                count = 1
        nextResult.append((count, curr))

        ret = ""
        for (x, y) in nextResult:
            ret += str(x)
            ret += str(y)

        return ret
