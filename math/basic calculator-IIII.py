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
