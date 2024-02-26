class Solution:

    def longestValidParentheses(self, s: str) -> int:
        # 1.遍历给字符串中的所有字符
        # 1.1若当前字符s[index]为左括号'('，将当前字符下标index入栈（下标稍后有其他用处），处理下一字符
        # 1.2若当前字符s[index]为右括号')'，判断当前栈是否为空
        # 1.2.1若栈为空，则accumulatedLen = 0，当前有效长度为0，处理下一字符（当前字符右括号下标不入栈）
        # 1.2.2若栈不为空，则出栈（由于仅左括号入栈，则出栈元素对应的字符一定为左括号，可与当前字符右括号配对），判断栈是否为空
        # 1.2.2.1若栈为空，则maxlen = max(maxlen, index-start+1)，更新当前最大匹配序列长度
        # 1.2.2.2若栈不为空，则maxlen = max(maxlen, i-栈顶元素值)，更新当前最大匹配序列长度
        stack = []
        result = 0
        tmp_result = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if not stack:
                    tmp_result = 0
                else:
                    start = stack.pop()
                    if not stack:
                        tmp_result += (i - start + 1)
                        result = max(tmp_result, result)
                    else:
                        result = max(i - stack[-1], result)
        return result
