import re

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return None

        operator = {'+': 2, '-': 2,
                    '(': 10, ')': 1}

        def validate_input(s):
            s = s.strip().replace(' ', '')
            # need to consider >=10, and no operator given
            comp = re.compile(r'[\+\-\(\)]|\d+')
            s = comp.findall(s)
            print(s)
            return s

        s = validate_input(s)
        stack_ele = []
        stack_ope = []

        def helper():
            num_2 = int(stack_ele.pop())
            num_1 = int(stack_ele.pop())
            ope = stack_ope.pop()
            if ope is '+':
                stack_ele.append(num_1+num_2)
            elif ope is '-':
                stack_ele.append(num_1-num_2)
            else:
                print(ope)
                print("ope exception happen")

        for e in s:
            if e in operator:
                if e is ')':
                    while stack_ope:
                        if stack_ope[-1] is '(':
                            stack_ope.pop()
                            break
                        helper()
                elif e is '(':
                    stack_ope.append(e)
                else:
                    if not stack_ope:
                        stack_ope.append(e)
                    else:
                        while stack_ope and operator.get(stack_ope[-1]) <= operator.get(e):
                            helper()
                        stack_ope.append(e)
            else:
                stack_ele.append(e)

        while stack_ope and stack_ele:
            helper()

        if len(stack_ele) == 1 and not stack_ope:
            return int(stack_ele.pop())
        else:
            print(stack_ele)
            print(stack_ope)

s = Solution()
print(s.calculate(" 2+(20-1)+(2-2) "))




