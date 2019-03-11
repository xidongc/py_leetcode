# 　特别hardeeee
class Solution(object):
    def fiiltediffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        output = []
        for i in range(len(input)):
            if input[i] in {'+','-','*'}:
                for a in self.diffWaysToCompute(input[:i]):
                    for b in self.diffWaysToCompute(input[i+1:]):
                        if input[i] == '+':
                            output.append(a+b)
                        elif input[i] == '-':
                            output.append(a-b)
                        else:
                            output.append(a*b)
        if not output:
            output.append(int(input))
        return output

s = Solution()
s.diffWaysToCompute('2*3-4*5')