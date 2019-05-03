# refer to https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
class Solution(object):

    def multiply(self, num1: str, num2: str) -> str:

        # corner case
        if len(num1) == 0 or len(num2) == 0:
            return '0'

        output = [0 for _ in range(len(num1) + len(num2))]

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                output[i + j] += (mul + output[i + j + 1]) // 10
                output[i + j + 1] = (mul + output[i + j + 1]) % 10

        i = 0
        while i < len(output) and output[i] == 0:
            i += 1

        return '0' if len(output[i:]) == 0 else "".join(map(str, output[i:]))
