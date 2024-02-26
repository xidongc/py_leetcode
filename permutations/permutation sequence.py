import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        def helper(result, k, n):
            print(k)
            if len(result) == n:
                return result
            elif len(result) > n:
                return

            tmp = 0
            for i in range(1, n + 1):
                if str(i) in result:
                    continue
                else:
                    if tmp < k <= tmp + math.factorial(n - 1 - len(result)):
                        result.append(str(i))
                        helper(result, k - tmp, n)
                    else:
                        tmp = math.factorial(n - 1 - len(result)) + tmp

        results = []
        helper(results, k, n)
        return "".join(results)
