dep
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