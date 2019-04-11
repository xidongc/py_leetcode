class Solution(object):

    def calculate(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        stack = list()
        operator = "+"
        num = 0
        i = 0

        while i < len(s):
            e = s[i]
            if e.isdigit():
                num *= 10
                num += ord(e) - ord("0")
            elif e == "(":
                cnt = 1
                for j in range(i + 1, len(s)):
                    if s[j] == "(":
                        cnt += 1
                    if s[j] == ")":
                        cnt -= 1
                    if cnt == 0:
                        break
                num = self.calculate(s[i + 1:j])
                print(num)
                i = j

            if (not e.isdigit() and not e.isspace()) or i == len(s) - 1:
                if operator == "+":
                    stack.append(num)
                elif operator == "-":
                    stack.append(-num)
                elif operator == "*":
                    stack.append(stack.pop() * num)
                elif operator == "/":
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)

                operator = e
                num = 0
            i += 1
        return sum(stack)