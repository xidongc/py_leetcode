class Solution(object):

    def validOutput(self, input):
        count = 0
        output = ""

        for i in input:
            if i == "(":
                count += 1
                output += i
            elif i == ")":
                if count > 0:
                    count -= 1
                    output += i

        output = list(output)
        output.reverse()
        input = "".join(output)
        count = 0
        output = ""

        for i in input:
            if i == ")":
                count += 1
                output += i
            elif i == "(":
                if count > 0:
                    count -= 1
                    output += i

        output = list(output)
        output.reverse()
        return "".join(output)


s = Solution()
input = "(()))))"
ret = s.validOutput(input)
print(ret)
