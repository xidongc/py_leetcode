# without "(" and ")"
class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        stack = list()
        operator = "+"
        num = 0

        for i, e in enumerate(s):
            if e.isdigit():
                num *= 10
                num += ord(e) - ord("0")
            if (not e.isdigit() and not e.isspace()) or i == len(s) - 1:
                if operator == "+":
                    stack.append(num)
                elif operator == "-":
                    stack.append(-num)
                elif operator == "*":
                    stack.append(stack.pop() * num)
                elif operator == "/":
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)

                operator = e
                num = 0
        return sum(stack)


# using recursive for "(" and ")"
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


# xidong's solution for calculator with "(" and ")"
class Solution(object):

    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0

        stack = list()
        num = 0
        operator = "+"

        for i, e in enumerate(s):
            if e.isdigit():
                num *= 10
                num += ord(e) - ord("0")
            if e is "(":
                stack.append("(")
            if not e.isdigit() and not e.isspace() or i == len(s) - 1:
                if operator is "+":
                    stack.append(num)
                elif operator is "-":
                    stack.append(-num)
                elif operator is "*":
                    stack.append(stack.pop() * num)
                elif operator is "/":
                    if stack[-1] // num < 0 and stack[-1] % num != 0:
                        stack.append(stack.pop() // num + 1)
                    else:
                        stack.append(stack.pop() // num)

                if e is not "(" and e is not ")":
                    num = 0
                    operator = e

            if e is ")":
                tmp = 0
                while len(stack) > 0 and stack[-1] != "(":
                    tmp += stack.pop()
                stack.pop()
                stack.append(tmp)
                num = 0
                operator = e

            print(stack)

        print(stack)

        return sum(stack)

