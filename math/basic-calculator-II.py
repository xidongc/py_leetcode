class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operator = {"+": 2, "-": 2,
                    "*": 1, "/": 1}

        def validate_input(s):
            if not s:
                return -1
            j = 0
            ret = []
            for i, e in enumerate(s):
                if e in operator:
                    ret.append(s[j:i])
                    ret.append(e)
                    j = i+1
            ret.append(s[j:])
            return ret

        s = validate_input(s)
        stack_ope = []
        stack_ele = []

        def helper(stack_ele):
            op = stack_ope.pop()
            num_2 = int(stack_ele.pop())
            num_1 = int(stack_ele.pop())
            if op is '*':
                stack_ele.append(num_1*num_2)
            elif op is '/':
                stack_ele.append(num_1//num_2)
            elif op is '+':
                stack_ele.append(num_1+num_2)
            elif op is '-':
                stack_ele.append(num_1-num_2)

        for e in s:
            if e in operator:
                if not stack_ope:
                    stack_ope.append(e)
                else:
                    while stack_ope and operator.get(stack_ope[-1]) <= operator.get(e):
                        helper(stack_ele)
                    stack_ope.append(e)
            else:
                stack_ele.append(e)

        while stack_ope:
            helper(stack_ele)

        if len(stack_ele) == 1 and not stack_ope:
            return int(stack_ele.pop())
        else:
            return -1


s = "3+4*3"
print(eval(s))