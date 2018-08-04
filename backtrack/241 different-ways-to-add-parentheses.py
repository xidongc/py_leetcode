# 　特别hardeeee
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        output = []
        for i in range(len(input)):
            c = input[i]
            # Since there would always be like 2 - 3 * 3 one operator split each other
            # Enter bt while operator
            if c == '+' or c == '-' or c == '*':
                for a in self.diffWaysToCompute(input[:i]):
                    for b in self.diffWaysToCompute(input[i+1:]):

                        output.append(a + b if c == '+' else(a - b if c == '-' else a * b))
        if not output:
            output.append(int(input))
        return output

s = Solution()
s.diffWaysToCompute('2*3-4*5')