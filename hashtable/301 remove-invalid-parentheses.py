# BFS
# def is_odd(n):
#     return n % 2 == 1
#
# filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# return filter iterator

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # # All the possible parentheses would be here
        # parenList = [s]
        # visitedList = []
        # res = set()
        # found = False
        # while parenList:
        #     curParen = parenList.pop(0)
        #     # If Valid in this level, stop keep searching deeper
        #     if self.isValid(curParen):
        #         res.add(curParen)
        #         found = True
        #     #     No new items added to queue anymore
        #     if found:
        #         continue
        #     for i in range(len(curParen)):
        #         c = curParen[i]
        #         if c != '(' and c != ')':
        #             continue
        #         newParen = curParen[:i] + curParen[i+1:]
        #         if newParen not in visitedList:
        #             visitedList.append(newParen)
        #             parenList.append(newParen)
        # return list(res)
        #  以上超时了，纯粹是python问题吧因为方法没有变
        def isValid(string):
            left = 0
            for ch in string:
                if ch == '(':
                    left += 1
                elif ch == ')':
                    if left:
                        left -= 1
                    else:
                        return False
            return left == 0
        parenSet = [s]
        # 循环很多很多次，第一次减一个，第二次在上一次基础上再减一个，也就是去掉两个
        # 如果filter出有valid，就返回这层所有valid setpali
        while True:
            valid = list(filter(isValid, parenSet))
            if valid:
                return valid
            # parentSet 去重
            parenSet = {string[:i] + string[i + 1:] for string in parenSet for i in range(len(string))}
            # print(parenSet)

s = Solution()
print(s.removeInvalidParentheses("(s)())()"))