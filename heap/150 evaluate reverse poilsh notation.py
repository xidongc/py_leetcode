class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        if not tokens:
            return 0
        for token in tokens:
            if token in ["+","-","*","/"]:
                num1 = stack.pop()
                num2 = stack.pop()
                # num2是前面那个数，num1是后面的呀，位置调一调
                if token == "+":
                    res = num2 + num1
                elif token == "-":
                    res = num2 - num1
                elif token == "*":
                    res = num2 * num1
                else:
                    # here take care of the case like "1/-22",
                    # in Python, it returns -1, while in
                    # Leetcode it should return 0
                    if num2 * num1 < 0 and num2 % num1 != 0:
                        res = num2 // num1 + 1
                    else:
                        res = num2 // num1
                stack.append(res)
            else:
                stack.append(int(token))
        return int(stack[-1])
#     -11不算isdigit()，不能用这个

s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# s.evalRPN(["0","3","/"])
#         stack = []
#         for token in tokens:
#             if token in ['+', '-', '*', '/']:
#                 num2 = stack.pop()
#                 num1 = stack.pop()
#                 # if token in ['+:','-','*']:
#                 res = str(int(eval(num1 + token + num2)))
#                 # else:
#                 # res = str(int(num1)//int(num2))
#                 stack.append(res)
#             else:
#                 stack.append(token)
#         return int(stack[-1])